import sys
import random

def cross_validation():
    subpages = int(sys.argv[1])
    resultsFile = open("cross-validation/"+str(subpages)+".txt", "w+")
    for i in range(100):
        current = random.sample(range(0, subpages), 2)
        resultsFile.write(str(current[0])+",")
        resultsFile.write(str(current[1])+"\n")

cross_validation()
