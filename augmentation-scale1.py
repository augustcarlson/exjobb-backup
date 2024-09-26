import os
import random
import numpy as np


def augmentation():
    os.mkdir("augmentation")
    print("Loading parameters...")
    chunkLengthFile = open("augmentation-parameters/chunk-times-scale1.txt")
    chunkLengthFileStr = chunkLengthFile.read()
    chunkLengths = chunkLengthFileStr.split("\n") 
    chunkLengths.pop(-1)
    interArrivalFile = open("augmentation-parameters/normalized-inter-arrivals-scale1.txt")   
    interArrivalFileStr = interArrivalFile.read()
    interArrivals = interArrivalFileStr.split("\n")
    interArrivals.pop(-1) 

    print("Augmenting")
    for folder in range(100):
        print("Folder", folder)
        os.mkdir("augmentation/"+str(folder))
        for trace in range(10):
            newSample = 0
            for sample in range(10):
                for i in range(1):#how many times is each trace duplicated and augmented
                    if folder >= 10:
                        filename = "../../data/dataset-231121/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        if newSample >= 10:
                            f = open("augmentation/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                        else:
                            f = open("augmentation/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                    else:
                        filename = "../../data/dataset-231121/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        if newSample >= 10:
                            f = open("augmentation/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                        else:
                            f = open("augmentation/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                        
                    newSample += 1

                    file = open(filename)
                    file_str = file.read()
                    s = file_str.split("\n")
                    chunkSizes = []
                    startTimes = []
                    chunkStart = True
                    currentChunkSize = 0
                    currentChunkEnd = 2*1000*1000*1000
                    for line in s:
                        parts = line.split(",")
                        if len(parts) < 3:
                            continue

                        if parts[1] == "s":
                            continue
                            
                        if chunkStart:
                            startTimes.append(float(parts[0]))
                            chunkStart = False
                        
                        if float(parts[0]) < currentChunkEnd:
                            currentChunkSize += float(parts[2])-52#Remove packet overhead
                        else:
                            chunkSizes.append(currentChunkSize)
                            currentChunkSize = 0
                            chunkStart = True
                            currentChunkEnd += 2*1000*1000*1000

                    startTimes.pop(0)

                    quality = 2

                    time = 0

                    for i in range(len(chunkSizes)):
                        chunkSize = chunkSizes[i]
                        if random.randint(0, 99) < 10:
                            qualityRandom = random.randint(0, 99)
                            if quality == 1:
                                if qualityRandom < 22:
                                    quality = 4
                                else:
                                    quality = 2
                            elif quality == 2:
                                if qualityRandom < 36:
                                    quality = 4
                                else:
                                    quality = 1
                            else:
                                if qualityRandom < 79:
                                    quality = 2
                                else:
                                    quality = 1

                        #Scale chunksize based on quality
                        chunkSize *= quality/4 

                        packetString = ""

                        #Pick chunk length
                        chunkLengthIndex = random.randint(0, len(chunkLengths)-1)
                        chunkLength = float(chunkLengths[chunkLengthIndex])

                        #Calculate required packets
                        packets = chunkSize/(1500-52)#-52
                        packets = int(packets+0.5) #Convert to whole packets

                        #Time per packet
                        defaultTimePerPacket = chunkLength/packets

                        #If gap between chunks, apply gap
                        if time < startTimes[i]:
                            time = startTimes[i]                   

                        while(True):
                            #Pick random factor from inter arrival times
                            interArrivalIndex = random.randint(0, len(interArrivals)-1)
                            interArrivalFactor = float(interArrivals[interArrivalIndex])

                            time += defaultTimePerPacket*interArrivalFactor

                            packetString += str(int(time))

                            if chunkSize > 1500-52:#-52 #1500-overhead per packet
                                packetString += ",r,1500"           
                                packetString += "\n"
                                f.write(packetString)
                                packetString = ""
                                chunkSize -= 1500-52#-52 per packet
                            else:
                                packetString+= ",r,"+str(int(chunkSize)+52) #+52 Packet overhead
                                packetString += "\n"
                                f.write(packetString)
                                packetString = ""
                                break

augmentation()

