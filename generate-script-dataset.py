import os

PATH="/data/dataset-231121/none"
#os.mkdir("offset-train")
#os.mkdir("offset-test")
#os.mkdir("models")

def offset_train_dataset_k1():
    print("k1")
    os.mkdir("offset-train/k1")
    for folder in range(100):
        print(folder)
        os.mkdir("offset-train/k1/"+str(folder))
        for trace in range(10):
            for sample in range(10):
                if folder >= 10:
                    filename = PATH+"/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                    f = open("offset-train/k1/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log", "w+")
                else:
                    filename = PATH+"/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                    f = open("offset-train/k1/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log", "w+")
                file = open(filename)
                file_str = file.read()
                s = file_str.split("\n")
                s.reverse()
                endTime = 0
                for line in s:
                    offset = 10*1000000000
                    parts = line.split(",")
                    if len(parts) < 3:
                        continue

                    if trace == 9:
                        break
                    
                    if endTime == 0:
                        endTime = float(parts[0])
                        
                    if float(parts[0]) > endTime - offset:
                        continue

                    time = endTime - offset - float(parts[0]) 

                    if time > 40 * 1000000000: # 40 second long trace 
                        break

                    f.write(str(time))
                    f.write(",")
                    f.write(str(parts[1]))
                    f.write(",")
                    f.write(str(parts[2]))
                    f.write(",")
                    f.write(str(parts[3]))
                    f.write("\n")

def offset_train_dataset_k2():
    print("k2")
    os.mkdir("offset-train/k2")
    for folder in range(100):
        print(folder)
        os.mkdir("offset-train/k2/"+str(folder))
        for trace in range(10):
            newSample = 0
            for sample in range(10):
                for i in range(2):
                    TRAINOFFSET = (1/3)*10*1000*1000*1000#+-3.333 seconds offset
                    if i == 0:
                        TRAINOFFSET*=-1
                        
                    TESTOFFSET = 0

                    if folder >= 10:
                        filename = PATH+"/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        if newSample >= 10:
                            f = open("offset-train/k2/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                        else:
                            f = open("offset-train/k2/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                    else:
                        filename = PATH+"/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        if newSample >= 10:
                            f = open("offset-train/k2/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                        else:
                            f = open("offset-train/k2/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                    newSample += 1
                    file = open(filename)
                    file_str = file.read()
                    s = file_str.split("\n")
                    s.reverse()
                    endTime = 0
                    for line in s:
                        offset = 10*1000000000
                        parts = line.split(",")
                        if len(parts) < 3:
                            continue

                        if endTime == 0:
                            endTime = float(parts[0])

                        if trace == 9:
                            #testoffset
                            break
                            offset += TESTOFFSET
                        else:
                            #trainoffset
                            offset += TRAINOFFSET
                        
                        if float(parts[0]) > endTime - offset:
                            continue

                        time = endTime - offset - float(parts[0]) 

                        if time > 40 * 1000000000: #40second long trace 
                            break

                        f.write(str(time))
                        f.write(",")
                        f.write(str(parts[1]))
                        f.write(",")
                        f.write(str(parts[2]))
                        f.write(",")
                        f.write(str(parts[3]))
                        f.write("\n")

def offset_train_dataset_k3():
    print("k3")
    os.mkdir("offset-train/k3")
    for folder in range(100):
        print(folder)
        os.mkdir("offset-train/k3/"+str(folder))
        for trace in range(10):
            newSample = 0
            for sample in range(10):
                for i in range(4):
                    TRAINOFFSET = (-6+(4*i))*1000*1000*1000
                        
                    TESTOFFSET = 0#-9*1000000000 + 2*i*1000000000 #-9,-7,-5,-3,-1,1,3,5,7,9

                    if folder >= 10:
                        filename = PATH+"/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        if newSample >= 10:
                            f = open("offset-train/k3/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                        else:
                            f = open("offset-train/k3/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                    else:
                        filename = PATH+"/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        if newSample >= 10:
                            f = open("offset-train/k3/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                        else:
                            f = open("offset-train/k3/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                    newSample += 1
                    file = open(filename)
                    file_str = file.read()
                    s = file_str.split("\n")
                    s.reverse()
                    endTime = 0
                    for line in s:
                        offset = 10*1000000000
                        parts = line.split(",")
                        if len(parts) < 3:
                            continue

                        if endTime == 0:
                            endTime = float(parts[0])

                        if trace == 9:
                            #testoffset
                            break
                            offset += TESTOFFSET
                        else:
                            #trainoffset
                            offset += TRAINOFFSET
                        
                        if float(parts[0]) > endTime - offset:
                            continue

                        time = endTime - offset - float(parts[0]) 

                        if time > 40 * 1000000000: #40second long trace 
                            break

                        f.write(str(time))
                        f.write(",")
                        f.write(str(parts[1]))
                        f.write(",")
                        f.write(str(parts[2]))
                        f.write(",")
                        f.write(str(parts[3]))
                        f.write("\n")

def offset_train_dataset_k4():
    print("k4")
    os.mkdir("offset-train/k4")
    for folder in range(100):
        print(folder)
        os.mkdir("offset-train/k4/"+str(folder))
        for trace in range(10):
            newSample = 0
            for sample in range(10):
                for i in range(8):
                    INCREMENT = 10/9
                    TRAINOFFSET = ((-7*INCREMENT)+(2*i*INCREMENT))*1000*1000*1000

                    TESTOFFSET = 0#-9*1000000000 + 2*i*1000000000 #-9,-7,-5,-3,-1,1,3,5,7,9

                    if folder >= 10:
                        filename = PATH+"/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        if newSample >= 10:
                            f = open("offset-train/k4/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                        else:
                            f = open("offset-train/k4/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                    else:
                        filename = PATH+"/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        if newSample >= 10:
                            f = open("offset-train/k4/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                        else:
                            f = open("offset-train/k4/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                    newSample += 1
                    file = open(filename)
                    file_str = file.read()
                    s = file_str.split("\n")
                    s.reverse()
                    endTime = 0
                    for line in s:
                        offset = 10*1000000000
                        parts = line.split(",")
                        if len(parts) < 3:
                            continue

                        if endTime == 0:
                            endTime = float(parts[0])

                        if trace == 9:
                            #testoffset
                            break
                            offset += TESTOFFSET
                        else:
                            #trainoffset
                            offset += TRAINOFFSET
                        
                        if float(parts[0]) > endTime - offset:
                            continue

                        time = endTime - offset - float(parts[0]) 

                        if time > 40 * 1000000000: #40second long trace 
                            break

                        f.write(str(time))
                        f.write(",")
                        f.write(str(parts[1]))
                        f.write(",")
                        f.write(str(parts[2]))
                        f.write(",")
                        f.write(str(parts[3]))
                        f.write("\n")

def offset_test_dataset():
    testOffsets = [-10,-8,-6,-4,-2,0,2,4,6,8,10]
    for currentOffset in testOffsets:
        TESTOFFSET = 1000*1000*1000*currentOffset #SECONDS TESTING OFFSET
        os.mkdir("offset-test/"+str(currentOffset))
        for folder in range(100):
            print(currentOffset,":",folder)
            os.mkdir("offset-test/"+str(currentOffset)+"/"+str(folder))
            for trace in range(10):
                for sample in range(10):
                    if folder >= 10:
                        filename = PATH+"/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        f = open("offset-test/"+str(currentOffset)+"/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log", "w+")
                    else:
                        filename = PATH+"/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        f = open("offset-test/"+str(currentOffset)+"/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log", "w+")

                    file = open(filename)
                    file_str = file.read()
                    s = file_str.split("\n")
                    s.reverse()
                    endTime = 0                    
                    for line in s:
                        offset = 10*1000*1000*1000#10 SECOND OFFSET DEFAULT
                        parts = line.split(",")
                        if len(parts) < 3:
                            continue

                        if endTime == 0:
                            endTime = float(parts[0])

                        if trace == 9:
                            #testoffset
                            offset += TESTOFFSET
                        
                        else:
                            break
                            
                        if float(parts[0]) > endTime - offset:
                            continue

                        time = endTime - offset - float(parts[0]) 

                        if time > 40 * 1000*1000*1000: #100second long trace 
                            break

                        f.write(str(time))
                        f.write(",")
                        f.write(str(parts[1]))
                        f.write(",")
                        f.write(str(parts[2]))
                        f.write(",")
                        f.write(str(parts[3]))
                        f.write("\n")

#offset_train_dataset_k1()
offset_train_dataset_k2()
offset_train_dataset_k3()
#offset_train_dataset_k4()

#offset_test_dataset()
