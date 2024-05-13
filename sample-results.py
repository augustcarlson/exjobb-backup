import matplotlib.pyplot as plt
import numpy as np

def sample_results_df():
    list = []
    samples = [10,9,8,7,6,5,4,3,2,1]
    subpages = [9,8,7,6,5,4,3]
    for sample in samples:
        file = open("outputs/df-video-samples-10-"+str(sample)+".txt")
        file_str = file.read()
        s = file_str.split("\n")
        line = s[96]
        accuracyStart = line.find("accuracy") + 9 
        accuracyString = line[accuracyStart:accuracyStart+4]
        accuracyFloat = float(accuracyString)
        accuracyFloat *= 100
        accuracyInt = int(accuracyFloat+0.5)
        list.append(accuracyInt)

    for subpage in subpages:
        file = open("outputs/df-video-samples-"+str(subpage)+"-1.txt")
        file_str = file.read()
        s = file_str.split("\n")
        line = s[96]
        accuracyStart = line.find("accuracy") + 9 
        accuracyString = line[accuracyStart:accuracyStart+4]
        accuracyFloat = float(accuracyString)
        accuracyFloat *= 100
        accuracyInt = int(accuracyFloat+0.5)
        list.append(accuracyInt)

    print(list)

def sample_results_rf():
    list = []
    samples = [10,9,8,7,6,5,4,3,2,1]
    subpages = [9,8,7,6,5,4,3]
    for sample in samples:
        file = open("outputs/rf-video-samples-10-"+str(sample)+".txt")
        file_str = file.read()
        s = file_str.split("\n")
        line = s[66]
        accuracyStart = line.find("accuracy") + 9 
        accuracyString = line[accuracyStart:accuracyStart+4]
        accuracyFloat = float(accuracyString)
        accuracyFloat *= 100
        accuracyInt = int(accuracyFloat+0.5)
        list.append(accuracyInt)

    for subpage in subpages:
        file = open("outputs/rf-video-samples-"+str(subpage)+"-1.txt")
        file_str = file.read()
        s = file_str.split("\n")
        line = s[66]
        accuracyStart = line.find("accuracy") + 9 
        accuracyString = line[accuracyStart:accuracyStart+4]
        accuracyFloat = float(accuracyString)
        accuracyFloat *= 100
        accuracyInt = int(accuracyFloat+0.5)
        list.append(accuracyInt)

    print(list)

def sample_results_df_default():
    list = []
    samples = [10,9,8,7,6,5,4,3,2,1]
    subpages = [9,8,7,6,5,4,3]
    for sample in samples:
        file = open("outputs/df-default-samples-10-"+str(sample)+".txt")
        file_str = file.read()
        s = file_str.split("\n")
        line = s[96]
        accuracyStart = line.find("accuracy") + 9 
        accuracyString = line[accuracyStart:accuracyStart+4]
        accuracyFloat = float(accuracyString)
        accuracyFloat *= 100
        accuracyInt = int(accuracyFloat+0.5)
        list.append(accuracyInt)

    for subpage in subpages:
        file = open("outputs/df-default-samples-"+str(subpage)+"-1.txt")
        file_str = file.read()
        s = file_str.split("\n")
        line = s[96]
        accuracyStart = line.find("accuracy") + 9 
        accuracyString = line[accuracyStart:accuracyStart+4]
        accuracyFloat = float(accuracyString)
        accuracyFloat *= 100
        accuracyInt = int(accuracyFloat+0.5)
        list.append(accuracyInt)

    print(list)

def sample_results_rf_default():
    list = []
    samples = [10,9,8,7,6,5,4,3,2,1]
    subpages = [9,8,7,6,5,4,3]
    for sample in samples:
        file = open("outputs/rf-default-samples-10-"+str(sample)+".txt")
        file_str = file.read()
        s = file_str.split("\n")
        line = s[67]
        accuracyStart = line.find("accuracy") + 9 
        accuracyString = line[accuracyStart:accuracyStart+4]
        accuracyFloat = float(accuracyString)
        accuracyFloat *= 100
        accuracyInt = int(accuracyFloat+0.5)
        list.append(accuracyInt)

    for subpage in subpages:
        file = open("outputs/rf-default-samples-"+str(subpage)+"-1.txt")
        file_str = file.read()
        s = file_str.split("\n")
        line = s[67]
        accuracyStart = line.find("accuracy") + 9 
        accuracyString = line[accuracyStart:accuracyStart+4]
        accuracyFloat = float(accuracyString)
        accuracyFloat *= 100
        accuracyInt = int(accuracyFloat+0.5)
        list.append(accuracyInt)

    print(list)

print("df-aug")
#sample_results_df()
print("---")
print("rf-aug")
sample_results_rf()
print("---")
print("df-default")
#sample_results_df_default()
print("---")
print("rf-default")
#sample_results_rf_default()


