import matplotlib.pyplot as plt
import numpy as np

FONTSIZE = 12 #CHANGE TO APPROPRIATE SIZE

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

def polished_offset_plot_df():
    offset = [-10,-8,-6,-4,-2,0,2,4,6,8,10]

    accuracyK1 = [2.8, 3.4, 3.4, 2.6, 8.8, 96.2, 9.2, 3.4, 1.0, 2.0, 1.4]
    accuracyK2 = [1.8, 7.0, 8.4, 95.2, 8.2, 3.8, 7.0, 94.8, 8.8, 5.6, 5.2]
    accuracyK3 = [5.2, 10.8, 95.4, 13.0, 96.4, 8.6, 95.2, 9.2, 96.4, 8.6, 4.2]
    accuracyK4 = [6.4, 94.0, 95.2, 96.2, 94.6, 9.8, 93.2, 94.2, 95.8, 96.0, 6.6]

    plt.plot(offset, accuracyK1, color='red', label="K=1")
    plt.plot(offset, accuracyK2, color='green', label="K=2")
    plt.plot(offset, accuracyK3, color='blue', label="K=3")
    plt.plot(offset, accuracyK4, color='black', label="K=4")

    plt.legend(loc="upper left", fontsize=FONTSIZE)
    #plt.title("DF")
    plt.xlabel("Offset (s)")
    plt.ylabel("Accuracy (%)")
    plt.grid(True)
    plt.ylim(0, 110)
    plt.yticks(np.arange(0, 110, 20), fontsize=FONTSIZE) 
    plt.xticks(np.arange(-9, 12, 3), fontsize=FONTSIZE) 
    plt.show()

def polished_offset_plot_rf():
    offset = [-10,-8,-6,-4,-2,0,2,4,6,8,10]
    
    accuracyK1 = [2.0, 7.2, 2.8, 16.2, 15.2, 62.4, 18.2, 15.6, 9.0, 9.6, 6.0]
    accuracyK2 = [4.8, 16.4, 23.6, 38.6, 24.0, 19.4, 19.8, 36.8, 31.0, 23.6, 11.2]
    accuracyK3 = [19.8, 8.8, 45.2, 14.8, 47.8, 12.4, 47.0, 15.2, 45.2, 11.2, 20.8]
    accuracyK4 = [15.6, 27.4, 25.6, 26.4, 24.4, 21.4, 22.2, 26.0, 28.0, 30.2, 16.0]

    plt.plot(offset, accuracyK1, color='red', label="K=1")
    plt.plot(offset, accuracyK2, color='green', label="K=2")
    plt.plot(offset, accuracyK3, color='blue', label="K=3")
    plt.plot(offset, accuracyK4, color='black', label="K=4")


    plt.legend(loc="upper left", fontsize=FONTSIZE)
    #plt.title("RF")

    plt.xlabel("Offset (s)")
    plt.ylabel("Accuracy (%)")
    plt.grid(True)
    plt.ylim(0, 110)
    plt.yticks(np.arange(0, 110, 20), fontsize=FONTSIZE) 
    plt.xticks(np.arange(-9, 12, 3), fontsize=FONTSIZE) 

    plt.show()

def polished_offset_plot_adapted_df():
    offset = [-10,-8,-6,-4,-2,0,2,4,6,8,10]
    
    # accuracyK1 = [2.6, 2.4, 4.2, 9.0, 51.0, 97.8, 53.8, 9.4, 7.2, 6.6, 5.4]
    # accuracyK2 = [7.8, 7.0, 17.0, 97.0, 62.0, 19.6, 65.8, 95.6, 20.6, 5.4, 8.0]
    # accuracyK3 = [17.6, 58.0, 99.0, 87.8, 99.0, 92.2, 99.0, 91.0, 99.2, 52.4, 18.6]
    # accuracyK4 = [55.8, 99.0, 99.4, 99.4, 98.8, 99.0, 99.0, 99.0, 99.0, 99.2, 54.8]

    # 4000 buckets
    accuracyK1 = [2, 2, 9, 15, 69, 98, 63, 14, 8, 8, 8]
    accuracyK2 = [11, 7, 34, 98, 81, 46, 82, 97, 26, 9, 11]
    accuracyK3 = [31, 74, 99, 96, 99, 99, 100, 98, 99, 74, 26]
    accuracyK4 = [68, 99, 99, 99, 99, 98, 99, 98, 99, 98, 65]
    #cross val
    # [[1, 2, 4, 13, 74, 98, 69, 14, 8, 7, 7], [8, 7, 30, 98, 73, 49, 84, 96, 27, 6, 8], [26, 63, 99, 96, 100, 94, 100, 96, 99, 62, 26], [72, 99, 100, 100, 100, 100, 100, 99, 100, 99, 65]]
    # [[1, 2, 4, 14, 73, 98, 68, 14, 8, 7, 7], [8, 7, 27, 97, 80, 45, 76, 97, 30, 6, 6], [16, 45, 92, 83, 97, 79, 95, 80, 94, 40, 13], [71, 99, 99, 99, 99, 99, 99, 98, 98, 98, 60]]
    # [[2, 2, 6, 17, 74, 97, 65, 12, 9, 9, 10], [8, 11, 30, 98, 83, 52, 81, 97, 33, 11, 8], [24, 75, 99, 98, 99, 98, 99, 98, 98, 72, 25], [77, 99, 100, 100, 100, 100, 100, 100, 100, 99, 70]]
    # [[2, 2, 5, 12, 70, 97, 73, 17, 11, 8, 8], [6, 8, 33, 99, 82, 53, 84, 98, 35, 6, 8], [25, 73, 98, 96, 99, 96, 99, 96, 98, 64, 22], [58, 98, 98, 98, 98, 99, 99, 98, 98, 98, 63]]
    # [[1, 2, 4, 14, 67, 96, 65, 10, 7, 10, 10], [6, 6, 30, 98, 80, 42, 79, 98, 29, 9, 9], [24, 71, 99, 96, 99, 95, 99, 98, 98, 65, 29], [69, 100, 99, 100, 100, 100, 100, 100, 100, 100, 64]]



    #epochs 200
    # accuracyK1 = [4, 4, 3, 7, 56, 99, 48, 7, 5, 7, 4]
    # accuracyK2 = [11, 11, 15, 98, 74, 19, 74, 99, 20, 6, 9]
    # accuracyK3 = [25, 68, 99, 97, 99, 95, 99, 96, 99, 69, 23]
    # accuracyK4 = [69, 100, 100, 100, 100, 99, 100, 100, 100, 100, 68]

    plt.plot(offset, accuracyK1, color='red', label="K=1")
    plt.plot(offset, accuracyK2, color='green', label="K=2")
    plt.plot(offset, accuracyK3, color='blue', label="K=3")
    plt.plot(offset, accuracyK4, color='black', label="K=4")

    #bullets
    # bulletsK1 = [0]
    # bulletsK2 = [-3.33, 3.33]
    # bulletsK3 = [-6, -2, 2, 6]
    # bulletsK4 = [-7.77, -5.55, -3.33, -1.11, 1.11, 3.33, 5.55, 7.77]

    # plt.scatter(bulletsK1, [1], color='red')
    # plt.scatter(bulletsK2, [4, 4], color='green')
    # plt.scatter(bulletsK3, [1, 1, 1, 1], color='blue')
    # plt.scatter(bulletsK4, [1, 1, 1, 1, 1, 1, 1, 1], color='black')

    plt.legend(loc="lower center", fontsize=FONTSIZE)
    #plt.title("RF")

    plt.xlabel("Offset (s)")
    plt.ylabel("Accuracy (%)")
    plt.grid(True)
    plt.ylim(0, 110)
    plt.yticks(np.arange(0, 110, 20), fontsize=FONTSIZE) 
    plt.xticks(np.arange(-9, 12, 3), fontsize=FONTSIZE) 

    plt.show()

def polished_offset_plot_adapted_rf():
    offset = [-10,-8,-6,-4,-2,0,2,4,6,8,10]
    
    accuracyK1 = [49.6, 36.8, 83.6, 66.8, 74.6, 94.2, 75.6, 68.2, 82.4, 36.4, 51.2]
    accuracyK2 = [82.0, 87.8, 82.8, 94.8, 96.6, 91.2, 97.0, 96.2, 81.2, 88.2, 76.2]
    accuracyK3 = [96.8, 97.6, 98.6, 98.6, 98.6, 98.8, 98.6, 98.2, 98.6, 97.8, 96.2]
    accuracyK4 = [99.0, 99.0, 99.0, 99.0, 99.2, 99.2, 99.2, 99.2, 99.2, 99.2, 99.0]

    #-#Epoch = 200#-#
    # accuracyK1 = [86, 79, 98, 99, 99, 100, 98, 99, 100, 88, 89]
    # accuracyK2 = [98, 98, 99, 100, 100, 100, 100, 100, 100, 100, 99]
    # accuracyK3 = [99, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    # accuracyK4 = [99, 100, 99, 99, 100, 100, 100, 100, 100, 100, 100]



    #bw1->bw1
    accuracyK1 = [20, 22, 33, 42, 49, 55, 49, 39, 31, 21, 17]
    accuracyK2 = [40, 52, 60, 68, 72, 73, 74, 69, 61, 55, 38]
    accuracyK3 = [70, 75, 80, 82, 84, 85, 85, 85, 82, 76, 66]
    accuracyK4 = [77, 80, 85, 86, 86, 87, 87, 87, 86, 84, 80]

    #bw2->bw2
    accuracyK1 = [41, 41, 56, 60, 70, 75, 71, 64, 58, 39, 40]
    accuracyK2 = [63, 72, 75, 82, 84, 83, 84, 84, 78, 73, 62]
    accuracyK3 = [81, 86, 90, 92, 92, 93, 91, 92, 92, 88, 81]
    accuracyK4 = [87, 91, 91, 93, 93, 93, 93, 92, 92, 92, 88]

    #bw4->bw4
    # accuracyK1 = [65, 57, 83, 83, 88, 93, 88, 83, 82, 58, 63]
    # accuracyK2 = [81, 87, 88, 93, 94, 93, 94, 94, 88, 87, 81]
    # accuracyK3 = [89, 92, 95, 94, 95, 95, 95, 94, 94, 92, 89]
    # accuracyK4 = [92, 95, 95, 94, 95, 95, 95, 95, 95, 94, 94]

    #bw8->bw8
    # accuracyK1 = [80, 60, 92, 91, 94, 98, 95, 93, 95, 62, 80]
    # accuracyK2 = [86, 92, 92, 97, 98, 98, 98, 98, 94, 94, 87]
    # accuracyK3 = [96, 98, 98, 98, 98, 98, 97, 97, 97, 97, 95]
    # accuracyK4 = [98, 99, 99, 99, 99, 99, 99, 99, 99, 99, 98]

    # #aug1->bw1 figure not yet generated
    accuracyK1 = [7, 10, 14, 20, 28, 26, 18, 14, 8, 6, 6]
    accuracyK2 = [21, 22, 29, 32, 30, 31, 30, 24, 21, 15, 12]
    accuracyK3 = [30, 35, 36, 38, 38, 38, 37, 36, 32, 27, 22]
    accuracyK4 = [34, 36, 38, 39, 40, 40, 40, 39, 37, 34, 28]

    #aug2->bw2
    # accuracyK1 = [26, 41, 44, 52, 57, 52, 48, 41, 28, 28, 19]
    # accuracyK2 = [46, 51, 58, 59, 58, 61, 59, 53, 48, 39, 32]
    # accuracyK3 = [57, 61, 61, 63, 64, 63, 63, 61, 57, 51, 44]
    # accuracyK4 = [64, 66, 66, 67, 66, 67, 65, 66, 62, 57, 52]

    #aug4->bw4
    # accuracyK1 = [41, 69, 67, 78, 84, 76, 74, 66, 44, 55, 38]
    # accuracyK2 = [74, 75, 83, 82, 80, 84, 81, 76, 74, 62, 54]
    # accuracyK3 = [81, 84, 84, 85, 85, 85, 85, 86, 80, 74, 68]
    # accuracyK4 = [86, 86, 87, 86, 86, 86, 87, 85, 83, 78, 73]

    #aug8->bw8
    # accuracyK1 = [58, 87, 77, 90, 95, 83, 87, 83, 54, 78, 46]
    # accuracyK2 = [92, 92, 96, 94, 93, 96, 94, 89, 92, 76, 73]
    # accuracyK3 = [96, 96, 97, 96, 97, 96, 97, 97, 96, 95, 91]
    # accuracyK4 = [99, 99, 98, 98, 98, 98, 98, 98, 98, 95, 94]

    plt.plot(offset, accuracyK1, color='red', label="K=1")
    plt.plot(offset, accuracyK2, color='green', label="K=2")
    plt.plot(offset, accuracyK3, color='blue', label="K=3")
    plt.plot(offset, accuracyK4, color='black', label="K=4")


    plt.legend(loc="lower center", fontsize=FONTSIZE)
    #plt.title("RF")

    plt.xlabel("Offset (s)")
    plt.ylabel("Accuracy (%)")
    plt.grid(True)
    plt.ylim(0, 110)
    plt.yticks(np.arange(0, 110, 20), fontsize=FONTSIZE) 
    plt.xticks(np.arange(-9, 12, 3), fontsize=FONTSIZE) 

    plt.show()

def polished_offset_plot_beauty():
    offset = [-10,-8,-6,-4,-2,0,2,4,6,8,10]
    
    accuracyK1 = [3.5, 2, 1.3, 3.6, 35.3, 99, 32.4, 4.6, 1.9, 6.7, 3.6]
    accuracyK2 = [2.7, 2.1, 2.4, 18.9, 14.9, 3.1, 4.6, 25.1, 3.3, 1.2, 2.3]
    accuracyK3 = [13, 23, 24.7, 23.6, 25.3, 22.9, 25.7, 23, 24.3, 18.2, 7.8]
    accuracyK4 = [6, 11.6, 13.3, 12.8, 12.2, 12.7, 13.4, 13.5, 12.9, 12.8, 9]

    plt.plot(offset, accuracyK1, color='red', label="K=1")
    plt.plot(offset, accuracyK2, color='green', label="K=2")
    plt.plot(offset, accuracyK3, color='blue', label="K=3")
    plt.plot(offset, accuracyK4, color='black', label="K=4")

    plt.legend(loc="upper right", fontsize=FONTSIZE)
    #plt.title("RF")

    plt.xlabel("Offset (s)")
    plt.ylabel("Accuracy (%)")
    plt.grid(True)
    plt.ylim(0, 110)
    plt.yticks(np.arange(0, 110, 20), fontsize=FONTSIZE) 
    plt.xticks(np.arange(-9, 12, 3), fontsize=FONTSIZE) 

    plt.show()

def plot_sample_length():
    x = [60, 50, 40, 30, 20, 10, 8, 6, 4, 2]
    rf_accuracy = [61.8, 65.4, 54.0, 63.6, 51.4, 54.0, 43.2, 38.4, 25.8, 19.2]
    df_accuracy = [93.2, 93.2, 91.6, 94.0, 94.4, 92.6, 93.2, 90.8, 81.2, 42.2]
    rf_adapted_accuracy = [99.2, 98.2, 95.6, 80.6, 56.2, 31.0, 35.8, 33.0, 44.6, 22.4]
    df_adapted_accuracy = [98.0, 98.4, 97.8, 97.4, 95.4, 95.2, 92.2, 92.2, 73.0, 13.8]
    bnb_accuracy = [97.78, 96.3, 96.07, 95.93, 95.19, 87.19, 80.44, 57.70, 11.48, 2.52]

    rf_adapted_200epochs = [100, 100, 99, 97, 74, 30, 24, 35, 73, 43]
    #rf_adapted_200epochs = [100, 100, 100, 98, 79, 31, 23, 30, 72, 51]
    df_adapted_200epochs = [99, 99, 98, 99, 99, 97, 95, 96, 92, 54]

    # plt.plot(x, rf_accuracy, color='red', label="RF")
    # plt.plot(x, df_accuracy, color='blue', label="DF")
    # plt.plot(x, rf_adapted_accuracy, color='green', label="Adapted RF")
    # plt.plot(x, df_adapted_accuracy, color='purple', label="Adapted DF")
    # plt.plot(x, bnb_accuracy, color='pink', label="Beauty and the Burst")

    plt.plot(x, rf_adapted_200epochs, color='red', label="Adapted RF 200")
    plt.plot(x, df_adapted_200epochs, color='blue', label="Adapted DF 200")

    plt.legend(loc="lower right", fontsize=FONTSIZE)
    plt.xlabel("Sample length (s)")
    plt.ylabel("Accuracy (%)")
    plt.grid(True)
    plt.yticks(np.arange(0, 110, 20), fontsize=FONTSIZE) 
    plt.xticks(np.arange(0, 70, 10), fontsize=FONTSIZE) 
    plt.ylim(0, 110)
    plt.xlim(0, 65)
    
    plt.show()

def plot_sample_count():
    x = [90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    # rf_accuracy = [57.6, 59.8, 60.4, 57.0, 61.0, 60.8, 53.2, 59.4, 55.6, 21.8, 22.2, 12.2, 7.6, 7.6, 7.0, 1.8, 2.4]
    # df_accuracy = [93.2, 93.2, 92.4, 92.0, 92.6, 90.8, 88.0, 88.2, 85.2, 66.8, 64.8, 60.6, 50.2, 46.0, 38.6, 3.4, 2.6]
    # rf_adapted_accuracy = [98.6, 98.8, 98.6, 98.2, 98.0, 98.2, 96.2, 96.0, 95.2, 92.2, 89.6, 81.0, 77.2, 43.8, 39.8, 6.6, 2.0]
    # df_adapted_accuracy = [98.2, 97.6, 97.0, 98.2, 96.6, 96.0, 96.6, 96.0, 94.6, 92.0, 89.8, 90.8, 85.0, 78.0, 62.8, 57.8, 28.4]
    # bnb_accuracy = [93.78, 96.3, 94.89, 95.26, 96, 95.41, 94.81, 92, 92.89, 96, 96.07, 94.83, 93.65, 92.89, 94, 92.33, 82]

    rf_adapted_accuracy_200 = [100, 100, 100, 100, 100, 100, 100, 99, 98, 96, 98, 98, 97, 99, 96, 96, 79]
    df_adapted_accuracy_200 = [99, 99, 100, 99, 99, 99, 99, 98, 98, 95, 94, 98, 96, 96, 96, 92, 24]

    # plt.plot(x, rf_accuracy, color='red', label="RF")
    # plt.plot(x, df_accuracy, color='blue', label="DF")
    # plt.plot(x, rf_adapted_accuracy, color='green', label="Adapted RF")
    # plt.plot(x, df_adapted_accuracy, color='purple', label="Adapted DF")
    # plt.plot(x, bnb_accuracy, color='pink', label="Beauty and the Burst")

    plt.plot(x, rf_adapted_accuracy_200, color='red', label="Adapted RF 200")
    plt.plot(x, df_adapted_accuracy_200, color='blue', label="Adapted DF 200")

    plt.legend(loc="lower right", fontsize=FONTSIZE)
    plt.xlabel("Sample count")
    plt.ylabel("Accuracy (%)")
    plt.grid(True)
    plt.yticks(np.arange(0, 110, 20), fontsize=FONTSIZE) 
    plt.xticks(np.arange(0, 100, 10), fontsize=FONTSIZE) 
    plt.ylim(0, 110)
    plt.xlim(0, 100)
    plt.show()

def plot_raw_offset():
    offset = [-10,-8,-6,-4,-2,0,2,4,6,8,10]
    
    accuracyRF = [2.0, 7.2, 2.8, 16.2, 15.2, 62.4, 18.2, 15.6, 9.0, 9.6, 6.0]
    accuracyDF = [2.8, 3.4, 3.4, 2.6, 8.8, 96.2, 9.2, 3.4, 1.0, 2.0, 1.4]
    accuracyRFaug = [49.6, 36.8, 83.6, 66.8, 74.6, 94.2, 75.6, 68.2, 82.4, 36.4, 51.2]
    accuracyDFaug = [2.6, 2.4, 4.2, 9.0, 51.0, 97.8, 53.8, 9.4, 7.2, 6.6, 5.4]
    accuracyBNB = [3.5, 2, 1.3, 3.6, 35.3, 99, 32.4, 4.6, 1.9, 6.7, 3.6]

    plt.plot(offset, accuracyRF, color='red', label="RF")
    plt.plot(offset, accuracyDF, color='green', label="DF")
    plt.plot(offset, accuracyRFaug, color='blue', label="Adapted RF")
    plt.plot(offset, accuracyDFaug, color='black', label="Adapted DF")
    plt.plot(offset, accuracyBNB, color='pink', label="BnB")

    plt.legend(loc="upper left", fontsize=FONTSIZE)
    #plt.title("RF")

    plt.xlabel("Offset (s)")
    plt.ylabel("Accuracy (%)")
    plt.grid(True)
    plt.ylim(0, 110)
    plt.yticks(np.arange(0, 110, 20), fontsize=FONTSIZE) 
    plt.xticks(np.arange(-9, 12, 3), fontsize=FONTSIZE) 

    plt.show()   

def plot_precision():
    threshold = [0, 0.11, 0.35, 0.53, 0.66, 0.75, 0.82, 0.87, 0.91, 0.93, 0.95, 0.96, 0.97, 0.98, 0.99]
    thresholdRF = [0, 0.11, 0.35, 0.53, 0.66]

    precisionRF = [59.5, 70.2, 86.8, 100, 100]
    precisionDF = [93.8, 93.8, 94.1, 95.2, 96.6, 98.1, 98.9, 99.3, 99.5, 99.6, 99.6, 99.7, 99.7, 99.7, 100]
    precisionRFaug = [97.9, 97.1, 97.1, 97.9, 98.9, 99.1, 99.2, 99.1, 99.6, 99.8, 99.9, 100, 100, 100, 100]
    precisionDFaug = [99.4, 99.4, 99.4, 99.7, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    #precisionBNB = []

    plt.plot(thresholdRF, precisionRF, color='red', label="RF")
    plt.plot(threshold, precisionDF, color='green', label="DF")
    plt.plot(threshold, precisionRFaug, color='blue', label="Adapted RF")
    plt.plot(threshold, precisionDFaug, color='black', label="Adapted DF")
    #plt.plot(threshold, precisionBNB, color='black', label="BnB")


    plt.legend(loc="lower right", fontsize=FONTSIZE)
    #plt.title("RF")

    plt.xlabel("Threshold")
    plt.ylabel("Precision (%)")
    plt.grid(True)
    plt.ylim(50, 110)
    plt.yticks(np.arange(50, 110, 10), fontsize=FONTSIZE) 
    plt.xticks(np.arange(0, 1.1, 0.1), fontsize=FONTSIZE) 

    plt.show()   
    
def plot_recall():
    threshold = [0, 0.11, 0.35, 0.53, 0.66, 0.75, 0.82, 0.87, 0.91, 0.93, 0.95, 0.96, 0.97, 0.98, 0.99]


    recallRF = [59.5, 24.5, 0.02, 0.008, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    recallDF = [100, 100, 99.7, 96.9, 93.4, 89.3, 86.9, 84.4, 82.2, 79.3, 77.2, 75.9, 73.6, 70.7, 67.5]
    recallRFaug = [100, 100, 100, 99.3, 97.3, 96.6, 94.6, 93.9, 92.9, 92.2, 91.8, 91.1, 90.1, 87.6, 84.5]
    recallDFaug = [100, 100, 100, 98.2, 96.9, 95.8, 94.9, 94.3, 93.6, 92.8, 92.5, 92.1, 91.8, 91.3, 90.6]
    #recallBNB = []

    plt.plot(threshold, recallRF, color='red', label="RF")
    plt.plot(threshold, recallDF, color='green', label="DF")
    plt.plot(threshold, recallRFaug, color='blue', label="Adapted RF")
    plt.plot(threshold, recallDFaug, color='black', label="Adapted DF")
    #plt.plot(offset, accuracyBNB, color='black', label="BnB")


    plt.legend(loc="lower right", fontsize=FONTSIZE)

    plt.xlabel("Threshold")
    plt.ylabel("Recall (%)")
    plt.grid(True)
    plt.ylim(0, 110)
    plt.yticks(np.arange(0, 110, 20), fontsize=FONTSIZE) 
    plt.xticks(np.arange(0, 1.1, 0.1), fontsize=FONTSIZE) 

    plt.show()   

def plot_rf_video_buckets():
    buckets = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]

    cbw = [99.0, 99.6, 99.2, 98.6, 99.0, 96.2, 90.8, 87.4, 83.4, 81.0, 69.4, 68.0, 62.0, 64.8, 67.4, 53.4, 65.8, 61.8, 71.6, 64.4]
    vbw1 = [39.2, 52.6, 58.4, 60.0, 63.4, 61.8, 59.2, 55.6, 58.6, 48.6, 44.6, 48.6, 42.6, 40.2, 37.4, 35.0, 33.6, 33.6, 30.6, 30.2]
    vbw2 = [60.6, 72.2, 78.6, 79.8, 82.6, 81.8, 77.4, 76.6, 76.4, 73.2, 74.0, 72.2, 73.2, 73.6, 73.2, 73.4, 73.4, 73.6, 72.8, 73.2]
    vbw4 = [90.4, 93.6, 94.8, 94.8, 95.6, 96.0, 94.8, 93.4, 89.0, 90.2, 91.2, 86.4, 91.2, 89.8, 91.8, 91.6, 91.2, 89.2, 89.2, 91.2]

    plt.plot(buckets, cbw, color='red', label="Constant bandwidth")
    plt.plot(buckets, vbw4, color='green', label="Scale 4 variable")
    plt.plot(buckets, vbw2, color='blue', label="Scale 2 variable")
    plt.plot(buckets, vbw1, color='purple', label="Scale 1 variable")

    plt.legend(loc="lower right", fontsize=FONTSIZE)

    plt.xlabel("Buckets")
    plt.ylabel("Accuracy (%)")
    plt.grid(True)
    plt.ylim(0, 110)
    plt.yticks(np.arange(0, 110, 20), fontsize=FONTSIZE) 
    plt.xticks(np.arange(0, 2100, 200), fontsize=FONTSIZE) 

    plt.show()  

def plot_df_video_buckets():
    buckets = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000]

    cbw = [96, 98, 98, 98, 100, 98, 97, 97, 98, 98, 99, 99, 99, 98, 98, 98, 99, 98, 98, 99]
    bw1 = [39, 46, 53, 60, 64, 70, 70, 74, 74, 67, 68, 68, 67, 66, 64, 67, 59, 60, 62, 63]
    bw2 = [60, 66, 73, 79, 78, 83, 86, 86, 83, 83, 84, 84, 81, 84, 82, 83, 83, 81, 81, 80]
    bw4 = [90, 93, 91, 94, 94, 93, 93, 96, 96, 94, 96, 95, 96, 95, 96, 95, 95, 95, 94, 96]
    bw8 = [94, 97, 96, 95, 98, 96, 97, 98, 98, 97, 98, 98, 97, 95, 98, 96, 97, 96, 98, 97]

    # 3000-7000
    # cbw:
    # [97, 97, 99, 99, 99, 98, 99, 99, 99]
    # bw1:
    # [67, 71, 71, 72, 67, 71, 68, 69, 63]
    # bw2:
    # [84, 83, 84, 86, 82, 86, 83, 84, 85]
    # bw4:
    # [92, 95, 95, 95, 96, 96, 96, 95, 96]
    # bw8:
    # [96, 98, 96, 95, 96, 97, 97, 96, 94]
    # cbw:
    # [97, 96, 98, 99, 99, 98, 99, 98, 98]
    # bw1:
    # [72, 70, 69, 72, 72, 67, 61, 59, 62]
    # bw2:
    # [85, 84, 83, 83, 83, 85, 84, 85, 82]
    # bw4:
    # [94, 97, 96, 94, 95, 96, 92, 95, 95]
    # bw8:
    # [96, 97, 97, 95, 97, 96, 91, 97, 96]

    plt.plot(buckets, cbw, color='red', label="Constant bandwidth")
    plt.plot(buckets, bw8, color='green', label="Scale 8 variable")
    plt.plot(buckets, bw4, color='yellow', label="Scale 4 variable")
    plt.plot(buckets, bw2, color='blue', label="Scale 2 variable")
    plt.plot(buckets, bw1, color='purple', label="Scale 1 variable")

    plt.legend(loc="lower right", fontsize=FONTSIZE)

    plt.xlabel("Buckets")
    plt.ylabel("Accuracy (%)")
    plt.grid(True)
    plt.ylim(0, 110)
    plt.yticks(np.arange(0, 110, 20), fontsize=FONTSIZE) 
    plt.xticks(np.arange(0, 10100, 1000), fontsize=FONTSIZE) 

    plt.show()

def plot_rf_video_epochs():
    epochs = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600]

    cbw = [98.6, 99.6, 99.8, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0]
    vbw1 = [61.0, 77.2, 82.8, 86.0, 85.2, 87.2, 87.8, 88.2, 87.2, 87.6, 88.2, 88.0, 88.8, 89.4, 88.8, 88.6, 88.8, 89.2, 89.4, 89.2]
    vbw2 = [80.4, 88.8, 91.6, 93.2, 92.4, 93.4, 94.0, 93.6, 94.2, 93.4, 94.0, 93.8, 94.6, 94.4, 94.2, 95.0, 94.2, 94.6, 95.0, 94.4]
    vbw4 = [95.6, 97.0, 97.4, 97.4, 97.8, 98.0, 97.8, 97.6, 97.8, 98.0, 98.0, 98.0, 97.8, 98.0, 98.0, 97.8, 98.2, 97.8, 98.2, 97.8]

    plt.plot(epochs, cbw, color='red', label="Constant bandwidth")
    plt.plot(epochs, vbw4, color='green', label="Scale 4 variable")
    plt.plot(epochs, vbw2, color='blue', label="Scale 2 variable")
    plt.plot(epochs, vbw1, color='purple', label="Scale 1 variable")

    plt.legend(loc="lower right", fontsize=FONTSIZE)

    plt.xlabel("Epochs")
    plt.ylabel("Accuracy (%)")
    plt.grid(True)
    plt.ylim(50, 110)
    plt.yticks(np.arange(50, 110, 10), fontsize=FONTSIZE) 
    plt.xticks(np.arange(0, 650, 50), fontsize=FONTSIZE) 

    plt.show()  

def plot_df_video_epochs():
    epochs = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600]

    cbw = [98, 99, 99, 100, 100, 99, 100, 99, 99, 100, 100, 99, 100, 100, 99, 99, 99, 100, 100, 99]
    vbw1 = [69, 72, 76, 77, 76, 74, 81, 79, 79, 77, 77, 79, 77, 80, 77, 78, 78, 78, 79, 79]
    vbw2 = [86, 89, 88, 86, 89, 89, 89, 89, 88, 88, 88, 88, 89, 90, 88, 88, 88, 89, 89, 89]
    vbw4 = [95, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 96, 97, 97, 97, 97]
    vbw8 = [97, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99]

    plt.plot(epochs, cbw, color='red', label="Constant bandwidth")
    plt.plot(epochs, vbw8, color='black', label="Scale 8 variable")
    plt.plot(epochs, vbw4, color='green', label="Scale 4 variable")
    plt.plot(epochs, vbw2, color='blue', label="Scale 2 variable")
    plt.plot(epochs, vbw1, color='purple', label="Scale 1 variable")

    plt.legend(loc="lower right", fontsize=FONTSIZE)

    plt.xlabel("Epochs")
    plt.ylabel("Accuracy (%)")
    plt.grid(True)
    plt.ylim(50, 110)
    plt.yticks(np.arange(50, 110, 10), fontsize=FONTSIZE) 
    plt.xticks(np.arange(0, 650, 50), fontsize=FONTSIZE) 

    plt.show()  

def plot_rf_aug_x20():
    x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    accuracy_aug4 = [83, 90, 92, 93, 94, 94, 94, 94, 94, 95, 96, 96, 96, 95, 96, 97, 97, 97, 97, 97]
    plt.plot(x, accuracy_aug4, color='red')

    plt.xlabel("Copies")
    plt.ylabel("Accuracy (%)")
    plt.grid(True)
    plt.yticks(np.arange(60, 110, 5), fontsize=FONTSIZE) 
    plt.xticks(np.arange(0, 22, 2), fontsize=FONTSIZE) 
    plt.ylim(60, 110)
    plt.xlim(0, 21)
    plt.show()




def plot_roc_curve():
    tpRF = [59.5, 24.5, 5.9, 2, 0.8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    tpDF = [93.8, 93.8, 93.7, 92.4, 90.5, 87.8, 86, 83.9, 81.9, 79.1, 77, 75.7, 73.5, 70.6, 67.5, 63.7]
    tpRFaug = [97.9, 97.9, 97.9, 97.3, 96.3, 95.7, 93.8, 93.2, 92.6, 92, 91.7, 91.1, 90.1, 87.6, 84.5, 79.4]
    tpDFaug = [99.4, 99.4, 99.4, 98, 96.9, 95.8, 94.9, 94.3, 93.6, 92.8, 92.5, 92.1, 91.8, 91.3, 90.6, 89.8]

    fpRF = [40.5, 10.4, 0.9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fpDF = [6.2, 6.2, 6, 4.7, 3.1, 1.7, 1, 0.6, 0.4, 0.3, 0.3, 0.2, 0.2, 0.2, 0, 0]
    fpRFaug = [2.1, 2.1, 2.1, 2, 1, 0.9, 0.8, 0.8, 0.4, 0.2, 0.1, 0, 0, 0, 0, 0]
    fpDFaug = [0.6, 0.6, 0.6, 0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
 
    plt.plot(fpRF, tpRF, color='red', label="RF")
    plt.plot(fpDF, tpDF, color='green', label="DF")
    plt.plot(fpRFaug, tpRFaug, color='blue', label="Adapted RF")
    plt.plot(fpDFaug, tpDFaug, color='black', label="Adapted DF")
    #plt.plot(offset, accuracyBNB, color='black', label="BnB")


    plt.legend(loc="lower right", fontsize=FONTSIZE)

    plt.xlabel("False positive rate (%)")
    plt.ylabel("True positive rate (%)")
    plt.grid(True)
    plt.ylim(0, 110)
    plt.xlim(0, 50)
    plt.yticks(np.arange(0, 110, 20), fontsize=FONTSIZE) 
    plt.xticks(np.arange(0, 50, 10), fontsize=FONTSIZE) 

    plt.show()    

def plot_roc_curve_scale1():
    tpRF = [45.4, 14.7, 3.2, 1.4, 0.8, 0.7, 0.4, 0.1, 0, 0, 0, 0, 0, 0, 0, 0]
    tpDF = [27.7, 27.5, 18.7, 10.3, 5.8, 4, 2.3, 1.7, 1.1, 0.9, 0.6, 0.4, 0.3, 0.2, 0.2, 0.2]
    tpRFaug = [59.8, 55.2, 34.5, 23.7, 17.3, 14.3, 11.7, 9.2, 7.1, 6.1, 4.8, 3.7, 3.1, 2.4, 1.7, 1.5]
    tpDFaug = [68, 68, 65, 56, 50, 43.7, 39.3, 34.8, 31.4, 29, 26.4, 23, 20.5, 18.4, 16.3, 14.6]

    fpRF = [54.6, 4.1, 0.3, 0.1, 0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fpDF = [72.3, 68.7, 21.8, 5.8, 2.3, 1, 0.7, 0.3, 0.2, 0, 0, 0, 0, 0, 0, 0]
    fpRFaug = [40.2, 24.3, 6.6, 1.8, 0.3, 0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fpDFaug = [32, 31.9, 22.7, 11.8, 5, 2.1, 1.3, 0.4, 0.2, 0.1, 0.1, 0, 0, 0, 0, 0]
 
    plt.plot(fpRF, tpRF, color='red', label="RF")
    plt.plot(fpDF, tpDF, color='green', label="DF")
    plt.plot(fpRFaug, tpRFaug, color='blue', label="Adapted RF")
    plt.plot(fpDFaug, tpDFaug, color='black', label="Adapted DF")
    #plt.plot(offset, accuracyBNB, color='black', label="BnB")


    plt.legend(loc="upper right", fontsize=FONTSIZE)

    plt.xlabel("False positive rate (%)")
    plt.ylabel("True positive rate (%)")
    plt.grid(True)
    plt.ylim(0, 110)
    plt.xlim(0, 110)
    plt.yticks(np.arange(0, 110, 20), fontsize=FONTSIZE) 
    plt.xticks(np.arange(0, 110, 20), fontsize=FONTSIZE) 

    plt.show() 

#plot_sample_length()
#plot_sample_length()
#plot_precision()
#plot_recall()
#plot_rf_video_buckets()
#plot_rf_video_epochs()
#plot_roc_curve()
#plot_roc_curve_scale1()


def offset_data_dump():
    #for -10,-4,0,4,10
    k4_300_40s_160 = [97,100,100,100,99]
    k4_300_40s_80 = [97,100,100,100,96]
    k4_30_40s_160 = [96,99,99,99,93]
    k4_30_40s_80 = [90,99,98,98,89]

    k4_30_100s_100 = [98,99,100,100,98]
    k4_300_100s_100 = [99,100,100,100,99]

    k1_300_40s_160 = [24,82,100,76,20]
    k1_30_40s_160 = [15,67,100,66,15]

    k1_300_100s_100 = [55,94,100,96,41]
    k1_30_100s_100 = [60,95,95,93,50]

    k1_30_40s_sample1 = [4,14,32,16,6]
    k1_30_100s_sample1 = [28,54,67,58,26]

    k4_30_20s =[53,96,68,83,26]
    k4_300_20s =[61,100,84,95,32]

    #-----#

    #dataset 231121 not updated rf
    #k1 [7, 14, 22, 33, 86, 96, 82, 42, 17, 6, 2], 
    #k2 [18, 33, 76, 96, 93, 92, 92, 88, 68, 38, 15], 
    #k3 [59, 93, 98, 97, 98, 96, 98, 97, 96, 92, 68], 
    #k4 [91, 98, 99, 98, 99, 99, 98, 98, 97, 97, 91]]

    #-----#
    #Updated RF

    #dataset 231121 rfmatrix80 
    #df
    #[[6, 7, 10, 14, 66, 96, 51, 13, 5, 1, 2], [9, 11, 23, 95, 74, 17, 60, 95, 16, 6, 10], [17, 53, 98, 88, 99, 88, 99, 88, 99, 54, 26], [61, 99, 99, 99, 98, 98, 99, 99, 100, 98, 48]]
    #rf
    #[[7, 9, 20, 34, 83, 99, 76, 25, 14, 6, 5], [18, 40, 86, 96, 94, 94, 95, 96, 81, 44, 18], [78, 99, 99, 100, 100, 98, 99, 98, 98, 95, 84], [97, 100, 100, 100, 100, 99, 99, 100, 100, 99, 97]]

    #dataset 231121 rfmatrix500
    #df
    #[[7, 8, 6, 10, 57, 96, 46, 8, 2, 2, 2], [11, 8, 28, 97, 71, 16, 64, 95, 13, 6, 7], [24, 58, 98, 91, 98, 90, 98, 89, 98, 56, 23], [63, 99, 99, 99, 98, 98, 98, 97, 98, 97, 41]]
    #rf
    #[[44, 40, 61, 79, 70, 92, 48, 77, 46, 58, 70], [58, 65, 71, 83, 85, 85, 77, 78, 71, 73, 73], [95, 96, 99, 97, 99, 97, 99, 99, 99, 95, 95], [99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 98]]

    #dataset 231121 rfmatrix500 epoch300
    #df
    #[[6, 7, 7, 9, 61, 98, 53, 8, 4, 2, 4], [9, 10, 24, 99, 74, 15, 73, 97, 22, 7, 10], [25, 63, 99, 96, 99, 93, 99, 92, 99, 63, 25], [77, 99, 100, 99, 100, 99, 99, 99, 99, 99, 66]]
    #rf
    #[[93, 42, 99, 87, 69, 100, 54, 98, 89, 61, 96], [100, 100, 100, 100, 99, 100, 100, 99, 99, 99, 98], [100, 99, 99, 99, 99, 99, 99, 99, 99, 99, 98], [99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 98]]

    #dataset 240104 variable bandwidth epoch30 rfmatrix80
    #df
    #[[3, 4, 5, 12, 46, 72, 46, 12, 4, 3, 4], [6, 7, 26, 54, 50, 39, 56, 61, 28, 12, 7], [14, 28, 54, 61, 65, 64, 62, 59, 53, 34, 18], [14, 37, 55, 61, 65, 67, 62, 58, 52, 40, 26]]
    #rf
    #[[5, 5, 6, 11, 31, 48, 34, 11, 4, 3, 2], [6, 11, 32, 43, 42, 34, 34, 36, 26, 11, 4], [18, 34, 49, 51, 49, 44, 42, 37, 33, 22, 12], [28, 54, 60, 58, 55, 50, 44, 36, 26, 20, 14]]

    #dataset 231212-0-5 constant defence
    #df
    #[[0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1], [1, 1, 1, 1, 1, 0, 1, 2, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0], [1, 1, 2, 1, 2, 0, 0, 0, 0, 0, 0]]
    #rf
    #[[1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1], [1, 1, 0, 2, 1, 1, 1, 1, 1, 0, 0], [1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 2, 1, 1, 0, 0, 1, 2]]

    #dataset 240104 varaible bandwidth epoch300 rfmatrix500
    #df
    #[[4, 5, 6, 14, 55, 79, 51, 15, 9, 8, 7], [9, 13, 31, 68, 61, 40, 59, 61, 29, 11, 8], [15, 32, 59, 66, 69, 69, 66, 60, 52, 37, 20], [23, 44, 57, 61, 61, 57, 52, 47, 40, 31, 20]]
    #rf
    #[[44, 62, 63, 79, 85, 89, 85, 80, 67, 59, 49], [70, 78, 86, 88, 88, 87, 87, 86, 76, 69, 60], [85, 88, 91, 90, 91, 90, 90, 88, 87, 81, 75], [88, 91, 91, 91, 91, 91, 90, 89, 87, 82, 77]]

    #dataset 240104 variable bandwidth rfmatrix500
    #df
    #[[2, 4, 4, 9, 48, 71, 42, 10, 5, 4, 4], [5, 9, 28, 61, 56, 42, 59, 64, 33, 12, 8], [13, 29, 49, 56, 60, 59, 55, 53, 49, 30, 16], [17, 41, 59, 69, 69, 70, 67, 63, 53, 42, 26]]
    #rf
    #[[27, 33, 35, 51, 55, 63, 54, 49, 36, 34, 28], [41, 55, 62, 72, 73, 72, 67, 63, 52, 40, 34], [60, 67, 76, 79, 80, 79, 78, 74, 69, 61, 55], [76, 81, 83, 83, 84, 84, 80, 78, 74, 69, 62]]

    #dataset-240118-0-3 variable bandwidth scale 3
    #df
    #[[5, 7, 6, 14, 55, 75, 41, 8, 4, 3, 4], [5, 7, 20, 51, 34, 23, 40, 36, 9, 5, 4], [15, 34, 59, 59, 63, 58, 64, 59, 59, 28, 15], [40, 68, 72, 72, 72, 72, 67, 69, 68, 66, 30]]
    #rf
    #[[27, 32, 35, 41, 41, 46, 37, 38, 28, 27, 21], [47, 53, 57, 61, 60, 59, 59, 57, 47, 47, 39], [60, 63, 71, 67, 72, 67, 74, 65, 69, 57, 53], [71, 76, 78, 77, 78, 79, 77, 78, 74, 70, 61]]

    #dataset-240121-0-3 variable bandwidth scale 2
    #df
    #[[3, 3, 3, 10, 34, 49, 34, 10, 5, 3, 3], [3, 6, 14, 31, 24, 17, 24, 24, 7, 2, 2], [9, 18, 32, 31, 37, 34, 35, 28, 26, 16, 5], [23, 45, 50, 54, 54, 49, 46, 46, 45, 39, 26]]
    #rf
    #[[17, 20, 20, 26, 24, 31, 25, 24, 19, 20, 16], [28, 31, 35, 42, 41, 43, 41, 40, 33, 28, 25], [40, 43, 50, 52, 58, 56, 58, 53, 54, 48, 43], [49, 58, 59, 60, 64, 65, 64, 66, 59, 57, 51]]

    #dataset-240124 variable bandwidth scale 1 6sample
    #df
    #[[2, 5, 5, 8, 23, 36, 25, 11, 4, 3, 1], [5, 6, 15, 30, 29, 25, 33, 32, 17, 7, 7], [10, 23, 37, 39, 44, 43, 46, 41, 36, 25, 11], [24, 40, 48, 51, 51, 52, 51, 49, 46, 38, 25]]
    #rf
    #[[9, 13, 13, 15, 15, 17, 15, 14, 11, 9, 8], [22, 28, 33, 37, 37, 40, 40, 37, 34, 31, 27], [38, 43, 49, 52, 56, 52, 54, 50, 48, 41, 38], [52, 58, 63, 65, 65, 66, 63, 61, 58, 56, 48]]

    #dataset-240104 varable bandwidth same start time 6sample compare with 240124 6sample
    #df
    #[[2, 4, 6, 9, 32, 63, 38, 9, 5, 3, 2], [5, 6, 19, 50, 44, 32, 43, 51, 18, 6, 5], [9, 21, 39, 43, 45, 41, 39, 38, 35, 20, 10], [13, 28, 41, 47, 51, 49, 44, 41, 35, 28, 16]]
    #rf
    #[[15, 15, 17, 20, 23, 28, 23, 23, 15, 14, 12], [30, 38, 41, 47, 53, 52, 50, 47, 38, 34, 28], [48, 53, 64, 65, 71, 66, 69, 60, 59, 50, 45], [54, 62, 66, 69, 70, 71, 67, 65, 57, 52, 46]]



    #---#

    #sample length 60s
    #RF100
    #DF

    #sample length 50s
    #RF99
    #DF

    #sample length 40s
    #RF97
    #DF

    #sample length 30s
    #RF97
    #DF

    #sample length 20s
    #RF
    #DF

    #sample length 10s
    #RF
    #DF

    #---#

#plot_offset_accuracy()
#plot_offset_accuracy_df()
#plot_offset_accuracy_df_fair()
#plot_offset_accuracy_rf_size5()
#plot_raw_offset()

#plot_df_video_epochs()
#polished_offset_plot_adapted_df()
#plot_df_video_buckets()

plot_rf_aug_x20()
