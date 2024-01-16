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

def plot_outputs():
    lists = []
    offsets = [-10,-8,-6,-4,-2,0,2,4,6,8,10]
    for k in range(1, 5): #k1-4
        currentList = []
        for offset in offsets:
            file = open("outputs/k"+str(k)+str(offset)+".txt")
            file_str = file.read()
            s = file_str.split("\n")
            line = s[7]
            accuracyStart = line.find("accuracy") + 9 
            accuracyString = line[accuracyStart:accuracyStart+4]
            accuracyInt = float(accuracyString)
            accuracyInt *= 100
            accuracyInt = int(accuracyInt+0.5)
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

plot_outputs()

