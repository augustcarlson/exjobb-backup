import os
import random

#read trace
#accumulate packets in chunks and put chunks in list(remove packet overhead)
#create output trace
#for each chunk in list pick random quality
#depending on quality, scale chunk size (/2 or /4)
#create packets by subtracting from chunk size(add packet overhead),
#   randomize time between packets depending on quality 

#TODO "s" augmentation
def augmentation():
    for folder in range(1):
        #os.mkdir("augmentation/"+str(folder))
        for trace in range(1):
            for sample in range(1):

                if folder >= 10:
                    filename = "dataset-231121/dataset-231121/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                    #f = open("augmentation/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log", "w+")
                else:
                    filename = "dataset-231121/dataset-231121/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                    #f = open("augmentation/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log", "w+")

                file = open(filename)
                file_str = file.read()
                s = file_str.split("\n")
                chunks = []
                startTimes = []
                currentChunkSize = 0
                currentChunkEnd = 2*1000*1000*1000
                for line in s:
                    parts = line.split(",")
                    if len(parts) < 3:
                        continue

                    #todo
                    if parts[1] == "s":
                        continue

                    if currentChunkSize == 0:
                        startTimes.append(float(parts[0]))

                    if float(parts[0]) < currentChunkEnd:
                        currentChunkSize += float(parts[2])-50#remove packet overhead
                    else:
                        chunks.append(currentChunkSize)
                        currentChunkSize = 0
                        currentChunkEnd += 2*1000*1000*1000

                startTimes.append(startTimes[-1]+2*1000*1000*1000)    
                quality = 2
                time = 0

                for i in range(len(chunks)):
                    chunk = chunks[i]
                    if random.randint(0, 99) < 10:#Tune random, quality switch
                        qualityRandom = random.randint(0, 99)
                        if quality == 1:
                            if qualityRandom < 27:
                                quality = 4
                            else:
                                quality = 2
                        elif quality == 2:
                            if qualityRandom < 45:
                                quality = 4
                            else:
                                quality = 1
                        else:
                            if qualityRandom < 21:
                                quality = 1
                            else:
                                quality = 2

                    chunk *= quality/4

                    packetString = ""
                    packets = chunk/(1500-50) #change to correct overhead
                    if packets < 3:
                        print(packets)
                    maxTime = (startTimes[i+1]-startTimes[i])/packets

                    while(True):
                        #append time,r,
                        if time < startTimes[i]:
                            time = startTimes[i]
                        time += random.randrange(1000, int(maxTime))#change 5000 to maxTime/X
                        packetString += str(int(time))+",r,"

                        #append size
                        if chunk > 1500-50: #1500-overhead per packet
                            packetString += "1500"           
                            packetString += "\n"
                            #f.write(packetString)
                            print(packetString)
                            packetString = ""
                            chunk -= 1500-50#-50 #fix overhead per packet
                        else:
                            packetString+= str(int(chunk+50)) #change to appropriate packet overhead
                            packetString += "\n"
                            #f.write(packetString)
                            print(packetString)
                            print("---")
                            packetString = ""
                            break
                    #break

augmentation()
