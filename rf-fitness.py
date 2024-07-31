#!/usr/bin/env python3

"""
Runs Robust FingerPrinting (RF) by Shen et al., from the paper "Subverting
Website Fingerprinting Defenses with Robust Traffic Representation", USENIX
Security 2023.

The implementation below of RF is based on:

https://github.com/robust-fingerprinting/RF

Modified to work with our dataset structure and splitting.
"""

import argparse
import os
import sys
import numpy as np
import math
import torch
import torch.nn as nn
import torch.utils.data as Data
import torch.nn.functional as F
from torch.autograd import Variable
from multiprocessing import Pool
import datetime
import csv

ap = argparse.ArgumentParser()
# dataset and its dimensions
ap.add_argument("-d", required=True, default="", help="root folder of client/server dataset")
ap.add_argument("-c", required=False, type=int, default=100,
    help="the number of monitored websites (=classes)")
ap.add_argument("-p", required=False, type=int, default=10,
    help="the number of subpages")
ap.add_argument("-s", required=False, type=int, default=10,
    help="the number of samples per subpage to load")
ap.add_argument("-w", required=False, type=int, default=10,
    help="number of workers for loading traces from disk")

ap.add_argument("--train", required=False, default=False,
    action="store_true", help="train model")

ap.add_argument("--bytes", required=False, default=False,
    action="store_true", help="count bytes instead of packets")

ap.add_argument("--sm", required=False, default="", help="save model to provided path")
ap.add_argument("--lm", required=False, default="", help="load model from provided path")

## extra output
ap.add_argument("--csv", required=False, default=None,
    help="save resulting metrics in provided path in csv format")
ap.add_argument("--extra", required=False, default="",
    help="value of extra column in csv output")

# experiment parameters
ap.add_argument("-f", required=False, type=int, default=0,
    help="the fold number (partition offset)")
args = vars(ap.parse_args())

EPOCH = 30
BATCH_SIZE = 200
LR = 0.0005

def now():
    return datetime.datetime.now().strftime("%H:%M:%S")

def main():
    dataset, labels = {}, {}
    if not os.path.isdir(args["d"]):
        sys.exit(f"{args['d']} is not a directory")

    if args["bytes"]:
        print(f"{now()} counting BYTES, not packets (not default RF)")
    else:
        print(f"{now()} counting PACKETS, not bytes (default RF)")

    print(f"{now()} starting to load dataset from {args['d']}")

    dataset, labels = load_dataset_star(
        args["d"],
        args["c"],
        args["p"],
        args["s"],
        log2tam
    )

    print(f"{now()} loaded {len(dataset)} items in dataset with {len(labels)} labels")

    split = split_dataset(args["c"], args["p"], args["s"], args["f"], labels)
    print(
        f"{now()} split {len(split['train'])} training, "
        f"{len(split['validation'])} validation, and "
        f"{len(split['test'])} testing"
    )

    #### Get data into expected format ####
    train_x = np.array([dataset[ID] for ID in split["train"]])
    train_y = np.array([labels[ID] for ID in split["train"]])
    #validation_x = np.array([dataset[ID] for ID in split["validation"]])
    #validation_y = np.array([labels[ID] for ID in split["validation"]])
    test_x = np.array([dataset[ID] for ID in split["test"]])
    test_y = np.array([labels[ID] for ID in split["test"]])

    #### RF ####
    model = getRF(args["c"])

    if args["lm"] != "":
        model = torch.load(args["lm"])
        print(f"loaded model from {args['lm']}")

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    if torch.cuda.is_available():
        print(f"{now()} using {torch.cuda.get_device_name(0)}")
        model.cuda()

    optimizer = torch.optim.Adam(params=model.parameters(), lr=LR, weight_decay=0.001)
    loss_func = torch.nn.CrossEntropyLoss()

    train_x = torch.unsqueeze(torch.from_numpy(train_x), dim=1).type(torch.FloatTensor)
    train_x = train_x.view(train_x.size(0), 1, 2, -1)
    train_y = torch.from_numpy(train_y).type(torch.LongTensor)

    train_data = Data.TensorDataset(train_x, train_y)
    train_loader = Data.DataLoader(dataset=train_data, batch_size=BATCH_SIZE, shuffle=True)

    # training
    model.train()
    if args["lm"] == "":
        for epoch in range(EPOCH):
            print(f"{now()} epoch {epoch}")

            adjust_learning_rate(optimizer, epoch)

            for step, (tr_x, tr_y) in enumerate(train_loader):
                batch_x = Variable(tr_x.cuda())
                batch_y = Variable(tr_y.cuda())
                output = model(batch_x)
                _, accuracy = get_result(output.cpu(), tr_y.cpu())

                del batch_x
                loss = loss_func(output, batch_y)
                del batch_y
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

                del output

                if step % 100 == 0:
                    print(epoch, step, accuracy, loss.item())

    if args["sm"] != "":
        torch.save(model, args["sm"])
        print(f"saved model to {args['sm']}")

    # testing
    test_x = torch.unsqueeze(torch.from_numpy(test_x), dim=1).type(torch.FloatTensor)
    test_x = test_x.view(test_x.size(0), 1, 2, -1)
    test_x = test_x.to(device)
    test_y = torch.squeeze(torch.from_numpy(test_y)).type(torch.LongTensor)

    test_data = Data.TensorDataset(test_x, test_y)
    test_loader = Data.DataLoader(dataset=test_data, batch_size=1, shuffle=False)

    model.eval()
    predictions = []
    p_labels = []
    with torch.no_grad():
        for v, (x, y) in enumerate(test_loader):
            out = model(x)#.cpu().squeeze().detach().numpy()
            index = F.softmax(out, dim=1).cpu().numpy()
            predictions.extend(index.tolist())
            p_labels.extend(y.data.numpy().tolist())

    print(f"{now()} made {len(predictions)} predictions with {len(p_labels)} labels")
    csvline = []
    threshold = np.append([0], 1.0 - 1 / np.logspace(0.05, 2, num=15, endpoint=True))
    threshold = np.around(threshold, decimals=4)
    for th in threshold:
        tp, fp, fn, accuracy, label_right, label_total = metrics(th, predictions, p_labels)
        print(
            f"\tthreshold {th:4.2}, "
            f"accuracy {accuracy:4.2}   "
            f"[tp {tp:>5}, fp {fp:>5}, fn {fn:>5}]"
        )
        if th == 0:
            print(f"\t\t", end="")
            n = 0
            for key, value in sorted(label_right.items(), key=lambda x: x[0]):
                r = value/label_total[key]
                print(f"{key:>2} {r:>5}, ", end=" ")
                n += 1
                if n == 10:
                    print("")
                    print(f"\t\t", end="")
                    n = 0
            print("")
        csvline.append([
            th, accuracy, tp, fp, fn, args["extra"]
        ])

    if args["csv"]:
        with open(args["csv"], "w", newline="") as csvfile:
            w = csv.writer(csvfile, delimiter=",")
            w.writerow(["th", "accuracy", "tp", "fp", "fn", "extra"])
            w.writerows(csvline)
        print(f"saved testing results to {args['csv']}")

    tp, fp, fn, accuracy, label_right, label_total = metrics(0, predictions, p_labels)
    print(1.0 - accuracy)

def parse_trace(fname, ID, extract_func):
        with open(fname, "r") as f:
           return (ID, extract_func(f.read()))

def load_dataset_star(folder, classes, subpages, samples, extract_func):
    labels = {}

    # starmap into todo
    todo = []
    for c in range(0,classes):
        for p in range(0,subpages):
            for s in range(0,samples):
                ID = to_file_label(c, p, s)
                labels[ID] = c
                # file format is {site}-{sample}.trace
                fname = f"{ID}.log"
                todo.append(
                    (os.path.join(folder, str(c), fname), ID, extract_func)
                )

    # starmap do results
    p = Pool(args["w"])
    results = p.starmap(parse_trace, todo)

    # assemble results
    data = {}
    for result in results:
        features = np.array(result[1])
        if len(features.shape) < 3:
            features = features[:, np.newaxis, :]
        data[result[0]] = features

    return data, labels

def to_file_label(c, sub, sample):
    return f"{int(c):04d}-{int(sub):04d}-{int(sample):04d}"

def split_dataset(
    websites, subpages, samples, fold, labels):
    '''Splits the dataset based on fold.

    The split is only based on IDs, not the actual data. The result is a 8:1:1
    split into training, validation, and testing.
    '''
    training = []
    validation = []
    testing = []

    # the split is made on subpages
    splitFile = open("cross-validation/"+str(subpages)+".txt")
    splitFile_str = splitFile.read()
    splitList = splitFile_str.split("\n")
    for c in range(0,websites):
        for p in range(0,subpages):
            for s in range(0,samples):
                ID = to_file_label(c, p, s)
                testIndex = int(splitList[c].split(",")[0])
                validationIndex = int(splitList[c].split(",")[1])
                if p == testIndex:
                    testing.append(ID)
                elif p == validationIndex:
                    validation.append(ID)
                else:
                    training.append(ID)



    # for c in range(0,websites):
    #     for p in range(0,subpages):
    #         for s in range(0,samples):
    #             ID = to_file_label(c, p, s)

    #             i = (p+fold) % subpages
    #             if i < subpages-2:
    #                 training.append(ID)
    #             elif i < subpages-1:
    #                 validation.append(ID)
    #             else:
    #                 testing.append(ID)

    split = {}
    split["train"] = training
    split["validation"] = validation
    split["test"] = testing
    return split

def metrics(threshold, predictions, labels):
    ''' Computes a range of metrics.

    For details on the metrics, see, e.g., https://www.cs.kau.se/pulls/hot/baserate/
    '''
    tp, fp, fn, accuracy = 0, 0, 0, 0.0

    # extended metric: per-class monitored stats
    label_right = {}
    label_total = {}

    for i in range(len(predictions)):
        label_pred = np.argmax(predictions[i])
        prob_pred = max(predictions[i])
        label_correct = labels[i]

        # total +1
        label_total[label_correct] = label_total.get(label_correct, 0) + 1
        
        # hack to get every label in the dict, not incrementing
        label_right[label_correct] = label_right.get(label_correct, 0)

        # either confident and correct,
        if prob_pred >= threshold and label_pred == label_correct:
            tp = tp + 1
            label_right[label_pred] = label_right.get(label_pred, 0) + 1
        # confident and wrong monitored label, or
        elif prob_pred >= threshold:
            fp = fp + 1
        # wrong because not confident enough
        else:
            fn = fn + 1

    accuracy = round(float(tp) / float(tp + fp + fn), 4)

    return tp, fp, fn, accuracy, label_right, label_total

max_matrix_len = 1800
maximum_load_time = 80.0

def log2tam(log):
    feature = [[0 for _ in range(max_matrix_len)], [0 for _ in range(max_matrix_len)]]

    s = log.split("\n")
    for line in s:
        parts = line.split(",")
        if len(parts) < 3:
            continue

        size = float(int(parts[2])) if args["bytes"] else 1
        # turn time into seconds
        time = float(parts[0])/float(1000*1000*1000)
        floc = 0 if "s" in parts[1] else 1 if "r" in parts[1] else -1

        if floc > -1:
            if time >= maximum_load_time:
                feature[floc][-1] += size
            else:
                idx = int(time * (max_matrix_len - 1) / maximum_load_time)
                feature[floc][idx] += size

    return feature


def adjust_learning_rate(optimizer, echo):
    lr = LR * (0.2 ** (echo / EPOCH))
    for para_group in optimizer.param_groups:
        para_group['lr'] = lr

def get_result(output, true_y):
    pred_y = torch.max(output, 1)[1].data.numpy().squeeze()
    accuracy = (pred_y == true_y.numpy()).sum().item() * 1.0 / float(true_y.size(0))
    return pred_y, accuracy

class RF(nn.Module):
    def __init__(self, features, num_classes=95, init_weights=True):
        super(RF, self).__init__()
        self.first_layer_in_channel = 1
        self.first_layer_out_channel = 32
        self.first_layer = make_first_layers()
        self.features = features
        self.class_num = num_classes
        self.classifier = nn.AdaptiveAvgPool1d(1)
        if init_weights:
            self._initialize_weights()

    def forward(self, x):
        x = self.first_layer(x)
        x = x.view(x.size(0), self.first_layer_out_channel, -1)
        x = self.features(x)
        x = self.classifier(x)
        x = x.view(x.size(0), -1)
        return x

    def _initialize_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                n = m.kernel_size[0] * m.kernel_size[1] * m.out_channels
                m.weight.data.normal_(0, math.sqrt(2. / n))
                if m.bias is not None:
                    m.bias.data.zero_()
            elif isinstance(m, nn.BatchNorm2d):
                m.weight.data.fill_(1)
                m.bias.data.zero_()
            elif isinstance(m, nn.Linear):
                m.weight.data.normal_(0, 0.01)
                m.bias.data.zero_()

def make_layers(cfg, in_channels=32):
    layers = []

    for i, v in enumerate(cfg):
        if v == 'M':
            layers += [nn.MaxPool1d(3), nn.Dropout(0.3)]
        else:
            conv1d = nn.Conv1d(in_channels, v, kernel_size=3, stride=1, padding=1)
            layers += [conv1d, nn.BatchNorm1d(v, eps=1e-05, momentum=0.1, affine=True), nn.ReLU()]
            in_channels = v

    return nn.Sequential(*layers)

def make_first_layers(in_channels=1, out_channel=32):
    layers = []
    conv2d1 = nn.Conv2d(in_channels, out_channel, kernel_size=(3, 6), stride=1, padding=(1, 1))
    layers += [conv2d1, nn.BatchNorm2d(out_channel, eps=1e-05, momentum=0.1, affine=True), nn.ReLU()]

    conv2d2 = nn.Conv2d(out_channel, out_channel, kernel_size=(3, 6), stride=1, padding=(1, 1))
    layers += [conv2d2, nn.BatchNorm2d(out_channel, eps=1e-05, momentum=0.1, affine=True), nn.ReLU()]

    layers += [nn.MaxPool2d((1, 3)), nn.Dropout(0.1)]

    conv2d3 = nn.Conv2d(out_channel, 64, kernel_size=(3, 6), stride=1, padding=(1, 1))
    layers += [conv2d3, nn.BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True), nn.ReLU()]

    conv2d4 = nn.Conv2d(64, 64, kernel_size=(3, 6), stride=1, padding=(1, 1))
    layers += [conv2d4, nn.BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True), nn.ReLU()]

    layers += [nn.MaxPool2d((2, 2)), nn.Dropout(0.1)]

    return nn.Sequential(*layers)

cfg = {
    'N': [128, 128, 'M', 256, 256, 'M', 512]
}

def getRF(num):
    model = RF(make_layers(cfg['N'] + [num]), num_classes=num)
    return model


if __name__ == "__main__":
    main()
