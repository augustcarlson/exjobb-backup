import matplotlib.pyplot as plt
import numpy as np

def plot_offset_accuracy_rf():
    offsets = [-10,-8,-6,-4,-2,0,2,4,6,8,10]
    
    accuracyK1 = [48,69,84,92,93,95,92,91,86,67,44]
    accuracyK2 = [79,88,92,95,95,95,94,94,89,84,75]
    accuracyK3 = [95,95,97,96,98,98,97,97,97,96,93]
    accuracyK4 = [96,96,98,99,98,99,99,100,99,98,96]

    accuracyK4300 = [98,99,100,100,100,100,100,100,100,99,99]
    accuracyK41000 = [96,97,98,98,98,98,99,99,98,98,96]

    plt.plot(offsets, accuracyK1, color='red')
    plt.plot(offsets, accuracyK2, color='green')
    plt.plot(offsets, accuracyK3, color='blue')
    plt.plot(offsets, accuracyK4, color='black')
    plt.plot(offsets, accuracyK4300, color='purple')
    plt.ylim(0, 110)
    plt.show()

def offset_results_df():
    lists = []
    offsets = [-10,-8,-6,-4,-2,0,2,4,6,8,10]
    for k in range(1, 5): #k1-4
        currentList = []
        for offset in offsets:
            file = open("outputs/df-video-k"+str(k)+str(offset)+".txt")
            file_str = file.read()
            s = file_str.split("\n")
            line = s[7]
            accuracyStart = line.find("accuracy") + 9 
            accuracyString = line[accuracyStart:accuracyStart+4]
            accuracyFloat = float(accuracyString)
            accuracyFloat *= 100
            accuracyInt = int(accuracyFloat+0.5)
            currentList.append(accuracyInt)
        lists.append(currentList)
    offsets = [-10,-8,-6,-4,-2,0,2,4,6,8,10]
    
    print(lists)
    #accuracyK1 = lists[0]
    #accuracyK2 = lists[1]
    #accuracyK3 = lists[2]
    #accuracyK4 = lists[3]

    #plt.plot(offsets, accuracyK1, color='red')
    #plt.plot(offsets, accuracyK2, color='green')
    #plt.plot(offsets, accuracyK3, color='blue')
    #plt.plot(offsets, accuracyK4, color='black')
    #plt.ylim(0, 110)
    #plt.show()

def offset_results_rf():
    lists = []
    offsets = [-10,-8,-6,-4,-2,0,2,4,6,8,10]
    for k in range(1, 5): #k1-4
        currentList = []
        for offset in offsets:
            file = open("outputs/rf-video-k"+str(k)+str(offset)+".txt")
            file_str = file.read()
            s = file_str.split("\n")
            line = s[7]
            accuracyStart = line.find("accuracy") + 9 
            accuracyString = line[accuracyStart:accuracyStart+4]
            accuracyFloat = float(accuracyString)
            accuracyFloat *= 100
            accuracyInt = int(accuracyFloat+0.5)
            currentList.append(accuracyInt)
        lists.append(currentList)

    print(lists)

def offset_results_df_default():
    lists = []
    offsets = [-10,-8,-6,-4,-2,0,2,4,6,8,10]
    for k in range(1, 5): #k1-4
        currentList = []
        for offset in offsets:
            file = open("outputs/df-default-k"+str(k)+str(offset)+".txt")
            file_str = file.read()
            s = file_str.split("\n")
            line = s[7]
            accuracyStart = line.find("accuracy") + 9 
            accuracyString = line[accuracyStart:accuracyStart+4]
            accuracyFloat = float(accuracyString)
            accuracyFloat *= 100
            accuracyInt = int(accuracyFloat+0.5)
            currentList.append(accuracyInt)
        lists.append(currentList)

    print(lists)

def offset_results_rf_default():
    lists = []
    offsets = [-10,-8,-6,-4,-2,0,2,4,6,8,10]
    for k in range(1, 5): #k1-4
        currentList = []
        for offset in offsets:
            file = open("outputs/rf-default-k"+str(k)+str(offset)+".txt")
            file_str = file.read()
            s = file_str.split("\n")
            line = s[7]
            accuracyStart = line.find("accuracy") + 9 
            accuracyString = line[accuracyStart:accuracyStart+4]
            accuracyFloat = float(accuracyString)
            accuracyFloat *= 100
            accuracyInt = int(accuracyFloat+0.5)
            currentList.append(accuracyInt)
        lists.append(currentList)

    print(lists)

def offset_results_rf_vbw():
    lists = []
    offsets = [-10,-8,-6,-4,-2,0,2,4,6,8,10]
    for k in range(1, 5): #k1-4
        currentList = []
        for offset in offsets:
            file = open("outputs/rf-video-k"+str(k)+str(offset)+".txt") #bw1, bw2, bw4,  bw8, aug1, aug2, aug4, aug8
            file_str = file.read()
            s = file_str.split("\n")
            line = s[7]
            accuracyStart = line.find("accuracy") + 9 
            accuracyString = line[accuracyStart:accuracyStart+4]
            accuracyFloat = float(accuracyString)
            accuracyFloat *= 100
            accuracyInt = int(accuracyFloat+0.5)
            currentList.append(accuracyInt)
        lists.append(currentList)

    print(lists)


def offset_results_rf_k4s_vbw():
    lists = []
    offsets = [-10,-8,-6,-4,-2,0,2,4,6,8,10]
    quals = ["cbw", "bw8", "bw4", "bw2", "bw1"]
    for train in quals:
        currentTrain = []
        for test in quals:
            currentTest = []
            for offset in offsets:
                file = open("outputs/"+train+"-"+test+"-rf-video-k4"+str(offset)+".txt") #cbw, bw1, bw2, bw4,  bw8, aug1, aug2, aug4, aug8
                file_str = file.read()
                s = file_str.split("\n")
                line = s[7]
                accuracyStart = line.find("accuracy") + 9 
                accuracyString = line[accuracyStart:accuracyStart+4]
                accuracyFloat = float(accuracyString)
                accuracyFloat *= 100
                accuracyInt = int(accuracyFloat+0.5)
                currentTest.append(accuracyInt)

            currentTrain.append(currentTest)
        lists.append(currentTrain)
    print("cbw, bw8, bw4, bw2, bw1")
    print(lists)

def offset_results_rf_k4s_augs():
    lists = []
    offsets = [-10,-8,-6,-4,-2,0,2,4,6,8,10]
    trains = ["cbw", "aug8", "aug4", "aug2", "aug1"]
    tests = ["cbw", "bw8", "bw4", "bw2", "bw1"]
    for train in trains:
        currentTrain = []
        for test in tests:
            currentTest = []
            for offset in offsets:
                file = open("outputs/"+train+"-"+test+"-rf-video-k4"+str(offset)+".txt") #cbw, bw1, bw2, bw4,  bw8, aug1, aug2, aug4, aug8
                file_str = file.read()
                s = file_str.split("\n")
                line = s[7]
                accuracyStart = line.find("accuracy") + 9 
                accuracyString = line[accuracyStart:accuracyStart+4]
                accuracyFloat = float(accuracyString)
                accuracyFloat *= 100
                accuracyInt = int(accuracyFloat+0.5)
                currentTest.append(accuracyInt)

            currentTrain.append(currentTest)
        lists.append(currentTrain)
    print("cbw, 8, 4, 2, 1")
    print(lists)

def offset_results_rf_k1s_vbw():
    lists = []
    offsets = [-10,-8,-6,-4,-2,0,2,4,6,8,10]
    quals = ["cbw", "bw8", "bw4", "bw2", "bw1"]
    for train in quals:
        currentTrain = []
        for test in quals:
            currentTest = []
            for offset in offsets:
                file = open("outputs/"+train+"-"+test+"-rf-video-k1"+str(offset)+".txt") #cbw, bw1, bw2, bw4,  bw8, aug1, aug2, aug4, aug8
                file_str = file.read()
                s = file_str.split("\n")
                line = s[7]
                accuracyStart = line.find("accuracy") + 9 
                accuracyString = line[accuracyStart:accuracyStart+4]
                accuracyFloat = float(accuracyString)
                accuracyFloat *= 100
                accuracyInt = int(accuracyFloat+0.5)
                currentTest.append(accuracyInt)

            currentTrain.append(currentTest)
        lists.append(currentTrain)
    print("cbw, bw8, bw4, bw2, bw1")
    print(lists)

def offset_results_rf_k1s_augs():
    lists = []
    offsets = [-10,-8,-6,-4,-2,0,2,4,6,8,10]
    trains = ["cbw", "aug8", "aug4", "aug2", "aug1"]
    tests = ["cbw", "bw8", "bw4", "bw2", "bw1"]
    for train in trains:
        currentTrain = []
        for test in tests:
            currentTest = []
            for offset in offsets:
                file = open("outputs/"+train+"-"+test+"-rf-video-k1"+str(offset)+".txt") #cbw, bw1, bw2, bw4,  bw8, aug1, aug2, aug4, aug8
                file_str = file.read()
                s = file_str.split("\n")
                line = s[7]
                accuracyStart = line.find("accuracy") + 9 
                accuracyString = line[accuracyStart:accuracyStart+4]
                accuracyFloat = float(accuracyString)
                accuracyFloat *= 100
                accuracyInt = int(accuracyFloat+0.5)
                currentTest.append(accuracyInt)

            currentTrain.append(currentTest)
        lists.append(currentTrain)
    print("cbw, 8, 4, 2, 1")
    print(lists)

offset_results_rf_k1s_augs()

# print("df-aug")
# #offset_results_df()
# print("---")
# print("rf-aug")
# offset_results_rf()
# print("---")
# print("df-default")
# #offset_results_df_default()
# print("---")
# print("rf-default")
# #offset_results_rf_default()


