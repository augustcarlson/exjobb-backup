
def get_params():
    chunkInterArrivals = []
    chunkLengths = []
    normalizedInterArrivals = []
    for folder in range(100):
        print(folder)
        for trace in range(10):
            for sample in range(1):
                if folder >= 10:
                    filename = "../../data/dataset-var/none-none-bw1/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                else:
                    filename = "../../data/dataset-var/none-none-bw1/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"

                file = open(filename)
                file_str = file.read()
                s = file_str.split("\n")
                currentChunkStartTime = 0
                previousTime = 0
                time = 0
                currentChunkInterArrivals = []
                chunkStartTimes = []
                currentChunkLengths = []
                for line in s:
                    parts = line.split(",")
                    if len(parts) < 3:
                        continue

                    time = float(parts[0])

                    if parts[1] == "s":
                        if 148 < int(parts[2]) < 155 and time - currentChunkStartTime > 1*1000*1000*1000:
                            if currentChunkStartTime == 0:
                                currentChunkStartTime = time
                                currentChunkInterArrivals = []
                            else:
                                chunkStartTimes.append(currentChunkStartTime)
                                currentChunkLengths.append(previousTime - currentChunkStartTime)
                                currentChunkStartTime = time
                                chunkInterArrivals.append(currentChunkInterArrivals)
                                currentChunkInterArrivals = []
                            previousTime = time
                        continue

                    currentChunkInterArrivals.append(time-previousTime)

                    previousTime = time

                chunkInterArrivals.append(currentChunkInterArrivals)

                while(len(currentChunkLengths) > (300-(trace*30))):
                    chunkStartTimesDiffs = chunk_start_time_diffs(chunkStartTimes)
                    smallestDiffIndex = chunkStartTimesDiffs.index(min(chunkStartTimesDiffs[1:]))
                    currentChunkLengths[smallestDiffIndex - 1] += currentChunkLengths[smallestDiffIndex]
                    currentChunkLengths.pop(smallestDiffIndex)
                    chunkInterArrivals[smallestDiffIndex - 1] += chunkInterArrivals[smallestDiffIndex]
                    chunkInterArrivals.pop(smallestDiffIndex)
                    chunkStartTimes.pop(smallestDiffIndex)
    
                chunkLengths += currentChunkLengths

    for interArrivals in chunkInterArrivals:
        if interArrivals:
            total = sum(interArrivals)
            avg = total/len(interArrivals)
            for interArrival in interArrivals:
                normalizedInterArrivals.append(interArrival/avg)

    normalizedInterArrivals.sort()
    file = open("augmentation-parameters/normalized-inter-arrivals1.txt", "w+")
    for value in normalizedInterArrivals:
        file.write(str(value))
        file.write("\n")

    chunkLengths.sort()
    file = open("augmentation-parameters/chunk-times1.txt", "w+")
    for value in chunkLengths:
        file.write(str(value))
        file.write("\n")   

def chunk_start_time_diffs(chunkStartTimes):
    chunkStartTimesDiffs = []
    for i in range(len(chunkStartTimes)):
        if not i == 0:
            chunkStartTimesDiffs.append(chunkStartTimes[i] - chunkStartTimes[i-1])     
        else:
            chunkStartTimesDiffs.append(chunkStartTimes[i])
    return chunkStartTimesDiffs
    

get_params()
