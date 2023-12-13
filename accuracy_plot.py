import matplotlib.pyplot as plt
import numpy as np

def plot_offset_accuracy():
    offset = [-10,-8,-6,-4,-2,0,2,4,6,8,10]
    accuracyDF = [3,9,18,73,91,93,92,66,23,11,4] 
    accuracyRF = [57,67,85,91,92,95,92,91,85,64,52]

    plt.plot(offset, accuracyRF)
    plt.show()

def plot_offset_accuracy_rf():
    offset = [-10,-8,-6,-4,-2,0,2,4,6,8,10]
    
    accuracyK1 = [48,69,84,92,93,95,92,91,86,67,44]
    accuracyK2 = [79,88,92,95,95,95,94,94,89,84,75]
    accuracyK3 = [95,95,97,96,98,98,97,97,97,96,93]
    accuracyK4 = [96,96,98,99,98,99,99,100,99,98,96]

    accuracyK4300 = [98,99,100,100,100,100,100,100,100,99,99]
    accuracyK41000 = [96,97,98,98,98,98,99,99,98,98,96]

    plt.plot(offset, accuracyK1, color='red')
    plt.plot(offset, accuracyK2, color='green')
    plt.plot(offset, accuracyK3, color='blue')
    plt.plot(offset, accuracyK4, color='black')
    plt.plot(offset, accuracyK4300, color='purple')
    plt.ylim(0, 110)
    plt.show()

def plot_offset_accuracy_df():
    offset = [-10,-8,-6,-4,-2,0,2,4,6,8,10]

    accuracyK1 = [2,8,24,67,90,92,89,66,26,8,4]
    accuracyK2 = [20,47,82,92,92,92,92,82,51,23,12]
    accuracyK3 = [51,74,88,88,90,90,91,89,90,80,54]
    accuracyK4 = [60,79,86,91,91,91,92,92,92,91,79]

    accuracyK4300 = [74,86,90,92,93,93,93,93,93,91,83]


    plt.plot(offset, accuracyK1, color='red')
    plt.plot(offset, accuracyK2, color='green')
    plt.plot(offset, accuracyK3, color='blue')
    plt.plot(offset, accuracyK4, color='black')
    plt.plot(offset, accuracyK4300, color='purple')
    plt.ylim(0, 110)
    plt.show()

def plot_offset_accuracy_rf_fair():
    offset = [-10,-8,-6,-4,-2,0,2,4,6,8,10]

    accuracyK1 = [48,72,90,94,96,100,96,95,91,61,36]
    accuracyK2 = [87,90,94,97,98,98,98,98,97,89,87]
    accuracyK3 = [96,99,100,99,100,98,98,98,99,97,95]
    accuracyK4 = [96,96,98,99,98,99,99,100,99,98,96]

    accuracyK3300 = [99,99,100,100,100,100,100,100,100,99,99]
    accuracyK4300 = [98,99,100,100,100,100,100,100,100,99,99]


    plt.plot(offset, accuracyK1, color='red')
    plt.plot(offset, accuracyK2, color='green')
    plt.plot(offset, accuracyK3, color='blue')
    plt.plot(offset, accuracyK4, color='black')
    plt.ylim(0, 110)
    plt.show()

def plot_offset_accuracy_df_fair():
    offset = [-10,-8,-6,-4,-2,0,2,4,6,8,10]

    accuracyK1 = [3,8,23,70,89,92,88,61,20,6,3]
    accuracyK2 = [15,37,72,92,93,90,92,83,49,21,12]
    accuracyK3 = [63,83,92,92,94,93,94,94,93,89,72]
    accuracyK4 = [60,79,86,91,91,91,92,92,92,91,79]

    accuracyK3300 = [67,83,93,91,93,92,94,93,93,86,71]
    accuracyK4300 = [74,86,90,92,93,93,93,93,93,91,83]


    plt.plot(offset, accuracyK1, color='red')
    plt.plot(offset, accuracyK2, color='green')
    plt.plot(offset, accuracyK3, color='blue')
    plt.plot(offset, accuracyK4, color='black')
    plt.ylim(0, 110)
    plt.show()

def plot_offset_accuracy_rf_size1():
    offset = [-10,-8,-6,-4,-2,0,2,4,6,8,10]

    accuracyK1 = [19,23,30,35,38,47,41,35,33,22,19]
    accuracyK2 = [34,48,58,64,66,67,66,62,57,44,31]
    accuracyK3 = [76,81,85,88,88,89,89,88,88,83,71]
    accuracyK4 = [85,89,91,90,91,91,91,91,91,89,83]

    plt.plot(offset, accuracyK1, color='red')
    plt.plot(offset, accuracyK2, color='green')
    plt.plot(offset, accuracyK3, color='blue')
    plt.plot(offset, accuracyK4, color='black')
    plt.ylim(0, 110)
    plt.show()

def plot_offset_accuracy_df_size1():
    offset = [-10,-8,-6,-4,-2,0,2,4,6,8,10]

    accuracyK1 = [0,0,0,0,0,0,0,0,0,0,0]
    accuracyK2 = [0,0,0,0,0,0,0,0,0,0,0]
    accuracyK3 = [0,0,0,0,0,0,0,0,0,0,0]
    accuracyK4 = [0,0,0,0,0,0,0,0,0,0,0]

    plt.plot(offset, accuracyK1, color='red')
    plt.plot(offset, accuracyK2, color='green')
    plt.plot(offset, accuracyK3, color='blue')
    plt.plot(offset, accuracyK4, color='black')
    plt.ylim(0, 110)
    plt.show()

def plot_offset_accuracy_rf_size3():
    offset = [-10,-8,-6,-4,-2,0,2,4,6,8,10]

    accuracyK1 = [45,63,80,87,91,92,92,89,81,63,45]
    accuracyK2 = [65,81,89,92,92,92,92,91,87,81,65]
    accuracyK3 = [87,89,91,92,91,93,92,92,92,90,86]
    accuracyK4 = [89,91,92,92,94,94,93,93,92,92,89]

    plt.plot(offset, accuracyK1, color='red')
    plt.plot(offset, accuracyK2, color='green')
    plt.plot(offset, accuracyK3, color='blue')
    plt.plot(offset, accuracyK4, color='black')
    plt.ylim(0, 110)
    plt.show()

def plot_offset_accuracy_df_size3():
    offset = [-10,-8,-6,-4,-2,0,2,4,6,8,10]

    accuracyK1 = [0,0,0,0,0,0,0,0,0,0,0]
    accuracyK2 = [0,0,0,0,0,0,0,0,0,0,0]
    accuracyK3 = [0,0,0,0,0,0,0,0,0,0,0]
    accuracyK4 = [0,0,0,0,0,0,0,0,0,0,0]

    plt.plot(offset, accuracyK1, color='red')
    plt.plot(offset, accuracyK2, color='green')
    plt.plot(offset, accuracyK3, color='blue')
    plt.plot(offset, accuracyK4, color='black')
    plt.ylim(0, 110)
    plt.show()

def plot_offset_accuracy_rf_size5():
    offset = [-10,-8,-6,-4,-2,0,2,4,6,8,10]

    accuracyK1 = [56,70,82,90,93,92,92,88,86,64,43]
    accuracyK2 = [74,87,90,92,93,93,93,93,90,87,75]
    accuracyK3 = [93,94,95,94,95,95,94,95,95,94,91]
    accuracyK4 = [94,95,96,96,97,96,97,98,97,98,97]

    plt.plot(offset, accuracyK1, color='red')
    plt.plot(offset, accuracyK2, color='green')
    plt.plot(offset, accuracyK3, color='blue')
    plt.plot(offset, accuracyK4, color='black')
    plt.ylim(0, 110)
    plt.show()

def plot_offset_accuracy_df_size5():
    offset = [-10,-8,-6,-4,-2,0,2,4,6,8,10]

    accuracyK1 = [0,0,0,0,0,0,0,0,0,0,0]
    accuracyK2 = [0,0,0,0,0,0,0,0,0,0,0]
    accuracyK3 = [0,0,0,0,0,0,0,0,0,0,0]
    accuracyK4 = [0,0,0,0,0,0,0,0,0,0,0]

    plt.plot(offset, accuracyK1, color='red')
    plt.plot(offset, accuracyK2, color='green')
    plt.plot(offset, accuracyK3, color='blue')
    plt.plot(offset, accuracyK4, color='black')
    plt.ylim(0, 110)
    plt.show()




#plot_offset_accuracy()
#plot_offset_accuracy_df()
#plot_offset_accuracy_df_fair()
plot_offset_accuracy_rf_size5()
