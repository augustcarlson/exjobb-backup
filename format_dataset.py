import os

def delete_png():
    for folder in range(92):
        for trace in range(10):
            for sample in range(100):
                if folder >= 10:
                    if sample >= 10:
                        filename = "export-dataset/client/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-00"+str(sample)+".png"
                    else:
                        filename = "export-dataset/client/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".png"
                else:
                    if sample >= 10:
                        filename = "export-dataset/client/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-00"+str(sample)+".png"
                    else:
                        filename = "export-dataset/client/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".png"

                if os.path.isfile(filename):
                    os.remove(filename)

def format_RF():
    for folder in range(100):
        for trace in range(7):
            for sample in range(3):
                if folder >= 10:
                    filename = "dataset-video/dataset-230922/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                else:
                    filename = "dataset-video/dataset-230922/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                file = open(filename)
                file_str = file.read()
                s = file_str.split("\n")
                s.reverse()
                endTime = 0
                true_sample = 3*trace + sample
                f = open("export-dataset/"+str(folder)+"-"+str(true_sample), "a")
                for line in s:
                    parts = line.split(",")
                    if len(parts) < 3:
                        continue

                    if endTime == 0:
                        endTime = float(parts[0])

                    if endTime - float(parts[0]) > 120000000000:
                        break

                    size = float(parts[2])
                    if parts[1] == 'r':
                        size *= -1
                    
                    f.write(str((endTime-float(parts[0]))/1000000000))
                    f.write("\t")
                    f.write(str(size))
                    f.write("\n")

def last2min():
    for folder in range(100):
        print(folder)
        os.mkdir("dataset-231121-last2min/none/"+str(folder))
        for trace in range(9):
            for sample in range(10):
                if folder >= 10:
                    filename = "dataset-231121/dataset-231121/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                    f = open("dataset-231121-last2min/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log", "w+")
                else:
                    filename = "dataset-231121/dataset-231121/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                    f = open("dataset-231121-last2min/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log", "w+")
                file = open(filename)
                file_str = file.read()
                s = file_str.split("\n")
                s.reverse()
                endTime = 0
                for line in s:
                    parts = line.split(",")
                    if len(parts) < 3:
                        continue

                    if endTime == 0:
                        endTime = float(parts[0])

                    if endTime - float(parts[0]) > 120000000000:
                        break

                    f.write(str(endTime-float(parts[0])))
                    f.write(",")
                    f.write(str(parts[1]))
                    f.write(",")
                    f.write(str(parts[2]))
                    f.write(",")
                    f.write(str(parts[3]))
                    f.write("\n")

def last1min():
    for folder in range(100):
        print(folder)
        os.mkdir("dataset-231121-last1min/none/"+str(folder))
        for trace in range(10):
            for sample in range(10):
                if folder >= 10:
                    filename = "dataset-231121/dataset-231121/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                    f = open("dataset-231121-last1min/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log", "w+")
                else:
                    filename = "dataset-231121/dataset-231121/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                    f = open("dataset-231121-last1min/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log", "w+")
                file = open(filename)
                file_str = file.read()
                s = file_str.split("\n")
                s.reverse()
                endTime = 0
                for line in s:
                    parts = line.split(",")
                    if len(parts) < 3:
                        continue

                    if endTime == 0:
                        endTime = float(parts[0])

                    if endTime - float(parts[0]) > 60000000000:
                        break

                    f.write(str(endTime-float(parts[0])))
                    f.write(",")
                    f.write(str(parts[1]))
                    f.write(",")
                    f.write(str(parts[2]))
                    f.write(",")
                    f.write(str(parts[3]))
                    f.write("\n")

def merge_datasets():
    for folder in range(100):
        print(folder)
        for trace in range(7):
            for sample in range(3):
                if folder >= 10:
                    filename = "dataset-video/dataset-230922/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                    f = open("dataset-video/dataset-231011/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample+4)+".log", "w+")
                else:
                    filename = "dataset-video/dataset-230922/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                    f = open("dataset-video/dataset-231011/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample+4)+".log", "w+")
                file = open(filename)
                file_str = file.read()
                s = file_str.split("\n")
                for line in s:
                    f.write(line)
                    f.write("\n")

def ten_seconds():
    for folder in range(100):
        print(folder)
        os.mkdir("20sec/none/"+str(folder))
        for trace in range(7):
            trueSample = 7*trace
            for sample in range(7):
                trueTrace = 0

                if folder >= 10:
                    filename = "dataset-231011-last2min/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                    if trueSample >= 10:
                        f = open("20sec/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trueTrace)+"-00"+str(trueSample)+".log", "w+")                              
                    else:
                        f = open("20sec/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trueTrace)+"-000"+str(trueSample)+".log", "w+")
                
                else:
                    filename = "dataset-231011-last2min/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
            
                    if trueSample >= 10:
                        f = open("20sec/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trueTrace)+"-00"+str(trueSample)+".log", "w+")                               
                    else:
                        f = open("20sec/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trueTrace)+"-000"+str(trueSample)+".log", "w+")

                file = open(filename)
                file_str = file.read()
                s = file_str.split("\n")
                fileLength = 20000000000 #20 sec
                endTime = 20000000000
                for line in s:
                    parts = line.split(",")
                    if len(parts) < 3:
                        continue

                    if int(parts[0]) >= endTime:
                        endTime += fileLength
                        trueTrace += 1
                        if folder >= 10:
                            if trueSample >= 10:
                                f = open("20sec/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trueTrace)+"-00"+str(trueSample)+".log", "w+")                              
                            else:
                                f = open("20sec/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trueTrace)+"-000"+str(trueSample)+".log", "w+")
                        
                        else:
                            if trueSample >= 10:
                                f = open("20sec/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trueTrace)+"-00"+str(trueSample)+".log", "w+")                               
                            else:
                                f = open("20sec/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trueTrace)+"-000"+str(trueSample)+".log", "w+")
                        
                    f.write(str(int(parts[0])-(endTime-fileLength)))
                    f.write(",")
                    f.write(str(parts[1]))
                    f.write(",")
                    f.write(str(parts[2]))
                    f.write(",")
                    f.write(str(parts[3]))
                    f.write("\n")
                trueSample += 1

def offset_dataset():
    for folder in range(100):
        print(folder)
        os.mkdir("x6dataset/none/"+str(folder))
        for trace in range(7):
            newSample = 0
            for sample in range(7):
                for i in range(6):
                    if folder >= 10:
                        filename = "dataset-231011-last2min/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        if newSample >= 10:
                            f = open("x6dataset/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                        else:
                            f = open("x6dataset/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                    else:
                        filename = "dataset-231011-last2min/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        if newSample >= 10:
                            f = open("x6dataset/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                        else:
                            f = open("x6dataset/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")

                    newSample += 1
                    file = open(filename)
                    file_str = file.read()
                    s = file_str.split("\n")
                    s.reverse()
                    endTime = 0
                    offset = 0
                    for line in s:
                        parts = line.split(",")
                        if len(parts) < 3:
                            continue

                        if endTime == 0:
                            endTime = int(parts[0])

                        # if trace != 6:
                        #     #trainoffset
                        #     offset = 10000000000
                        
                        if endTime - int(parts[0]) < offset :
                            continue

                        if endTime - int(parts[0]) > 120000000000 + offset:
                            break

                        f.write(str(endTime-int(parts[0])-offset))
                        f.write(",")
                        f.write(str(parts[1]))
                        f.write(",")
                        f.write(str(parts[2]))
                        f.write(",")
                        f.write(str(parts[3]))
                        f.write("\n")

def datasetx6():
    for folder in range(100):
        print(folder)
        os.mkdir("x10dataset/none/"+str(folder))
        for trace in range(7):
            newSample = 0
            for sample in range(7):
                for i in range(10):#x10
                    if folder >= 10:
                        filename = "offset-test/0/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        if newSample >= 10:
                            f = open("x10dataset/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                        else:
                            f = open("x10dataset/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                    else:
                        filename = "offset-test/0/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        if newSample >= 10:
                            f = open("x10dataset/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                        else:
                            f = open("x10dataset/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")

                    newSample += 1
                    file = open(filename)
                    file_str = file.read()
                    s = file_str.split("\n")
                    for line in s:
                        parts = line.split(",")
                        if len(parts) < 3:
                            continue

                        f.write(str(parts[0]))
                        f.write(",")
                        f.write(str(parts[1]))
                        f.write(",")
                        f.write(str(parts[2]))
                        f.write(",")
                        f.write(str(parts[3]))
                        f.write("\n")

def offset_dataset_split():
    for folder in range(100):
        print(folder)
        os.mkdir("split/none/"+str(folder))
        for trace in range(7):
            newSample = 0
            for sample in range(7):
                #for i in range(6):
                    if folder >= 10:
                        filename = "dataset-231011/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        if newSample >= 10:
                            f = open("split/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                        else:
                            f = open("split/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                    else:
                        filename = "dataset-231011/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        if newSample >= 10:
                            f = open("split/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                        else:
                            f = open("split/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")

                    newSample += 1
                    file = open(filename)
                    file_str = file.read()
                    s = file_str.split("\n")
                    s.reverse()
                    endTime = 0
                    offset = 0
                    for line in s:
                        parts = line.split(",")
                        if len(parts) < 3:
                            continue

                        if trace == 6:
                            #testoffset
                            offset = 20000000
                        
                        if endTime == 0:
                            endTime = int(parts[0]) - offset

                        if endTime < int(parts[0]):
                            continue

                        if endTime - int(parts[0]) > 120000000000:
                            break

                        f.write(str(endTime-int(parts[0])))
                        f.write(",")
                        f.write(str(parts[1]))
                        f.write(",")
                        f.write(str(parts[2]))
                        f.write(",")
                        f.write(str(parts[3]))
                        f.write("\n")

def offset_test_dataset_last1min():
    testOffsets = [-10,-8,-6,-4,-2,0,2,4,6,8,10]
    for currentOffset in testOffsets:
        TESTOFFSET = 1000*1000*1000*currentOffset #SECONDS TESTING OFFSET
        for folder in range(100):
            print(currentOffset,":",folder)
            os.mkdir("offset-test-231121-40/"+str(currentOffset)+"/"+str(folder))
            for trace in range(10):
                for sample in range(10):
                    if folder >= 10:
                        filename = "dataset-231121-last1min/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        f = open("offset-test-231121-40/"+str(currentOffset)+"/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log", "w+")
                    else:
                        filename = "dataset-231121-last1min/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        f = open("offset-test-231121-40/"+str(currentOffset)+"/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log", "w+")

                    file = open(filename)
                    file_str = file.read()
                    s = file_str.split("\n")
                    for line in s:
                        offset = 10*1000*1000*1000#10 SECOND OFFSET DEFAULT
                        parts = line.split(",")
                        if len(parts) < 3:
                            continue

                        if trace == 9:
                            #testoffset
                            offset += TESTOFFSET
                        
                        if float(parts[0]) < offset:
                            continue

                        time = float(parts[0]) - offset

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

def offset_test_dataset_last2min():
    testOffsets = [-10,-8,-6,-4,-2,0,2,4,6,8,10]
    for currentOffset in testOffsets:
        TESTOFFSET = 1000*1000*1000*currentOffset #SECONDS TESTING OFFSET
        for folder in range(100):
            print(currentOffset,":",folder)
            os.mkdir("offset-test-231121-100/"+str(currentOffset)+"/"+str(folder))
            for trace in range(9):
                for sample in range(10):
                    if folder >= 10:
                        filename = "dataset-231121-last2min/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        f = open("offset-test-231121-100/"+str(currentOffset)+"/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log", "w+")
                    else:
                        filename = "dataset-231121-last2min/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        f = open("offset-test-231121-100/"+str(currentOffset)+"/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log", "w+")

                    file = open(filename)
                    file_str = file.read()
                    s = file_str.split("\n")
                    for line in s:
                        offset = 10*1000*1000*1000#10 SECOND OFFSET DEFAULT
                        parts = line.split(",")
                        if len(parts) < 3:
                            continue

                        if trace == 8:
                            #testoffset
                            offset += TESTOFFSET
                        
                        if float(parts[0]) < offset:
                            continue

                        time = float(parts[0]) - offset

                        if time > 100 * 1000*1000*1000: #100second long trace 
                            break

                        f.write(str(time))
                        f.write(",")
                        f.write(str(parts[1]))
                        f.write(",")
                        f.write(str(parts[2]))
                        f.write(",")
                        f.write(str(parts[3]))
                        f.write("\n")

def offset_all_dataset_last2min():
    for folder in range(100):
        print(folder)
        os.mkdir("offset-train/none/"+str(folder))
        for trace in range(7):
            newSample = 0
            for sample in range(7):
                for i in range(10):
                    TRAINOFFSET = -10*1000000000 + 2*i*1000000000 #-10,-8,-6,-4,-2,2,4,6,8,10
                    if TRAINOFFSET >= 0: #to skip offset = 0
                        TRAINOFFSET += 2*1000000000
                    TESTOFFSET = 0#-9*1000000000 + 2*i*1000000000 #-9,-7,-5,-3,-1,1,3,5,7,9

                    if folder >= 10:
                        filename = "dataset-231011-last2min/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        if newSample >= 10:
                            f = open("offset-train/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                        else:
                            f = open("offset-train/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                    else:
                        filename = "dataset-231011-last2min/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        if newSample >= 10:
                            f = open("offset-train/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                        else:
                            f = open("offset-train/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                    newSample += 1
                    file = open(filename)
                    file_str = file.read()
                    s = file_str.split("\n")
                    for line in s:
                        offset = 10*1000000000
                        parts = line.split(",")
                        if len(parts) < 3:
                            continue

                        if trace == 6:
                            #testoffset
                            offset += TESTOFFSET
                        else:
                            #testoffset
                            offset += TRAINOFFSET
                        
                        if float(parts[0]) < offset:
                            continue

                        time = float(parts[0]) - offset

                        if time > 100 * 1000000000: #100second long trace 
                            break

                        f.write(str(time))
                        f.write(",")
                        f.write(str(parts[1]))
                        f.write(",")
                        f.write(str(parts[2]))
                        f.write(",")
                        f.write(str(parts[3]))
                        f.write("\n")

def offset_train_dataset_last2min_k1():
    print("k1")
    for folder in range(100):
        print(folder)
        os.mkdir("offset-train/k12min/"+str(folder))
        for trace in range(9):
            for sample in range(10):
                if folder >= 10:
                    filename = "dataset-231121-last2min/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                    f = open("offset-train/k12min/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log", "w+")
                else:
                    filename = "dataset-231121-last2min/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                    f = open("offset-train/k12min/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log", "w+")
                file = open(filename)
                file_str = file.read()
                s = file_str.split("\n")
                for line in s:
                    offset = 10*1000000000
                    parts = line.split(",")
                    if len(parts) < 3:
                        continue
                    
                    if float(parts[0]) < offset:
                        continue

                    time = float(parts[0]) - offset

                    if time > 100 * 1000000000: #100second long trace 
                        break

                    f.write(str(time))
                    f.write(",")
                    f.write(str(parts[1]))
                    f.write(",")
                    f.write(str(parts[2]))
                    f.write(",")
                    f.write(str(parts[3]))
                    f.write("\n")

def offset_train_dataset_last1min_k1():
    print("k1")
    for folder in range(100):
        print(folder)
        os.mkdir("offset-train/k11min/"+str(folder))
        for trace in range(10):
            for sample in range(10):
                if folder >= 10:
                    filename = "dataset-231121-last1min/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                    f = open("offset-train/k11min/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log", "w+")
                else:
                    filename = "dataset-231121-last1min/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                    f = open("offset-train/k11min/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log", "w+")
                file = open(filename)
                file_str = file.read()
                s = file_str.split("\n")
                for line in s:
                    offset = 10*1000000000
                    parts = line.split(",")
                    if len(parts) < 3:
                        continue
                    
                    if float(parts[0]) < offset:
                        continue

                    time = float(parts[0]) - offset

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

def offset_train_dataset_last2min_k2():
    print("k2")
    for folder in range(100):
        print(folder)
        os.mkdir("offset-train/k2size5/"+str(folder))
        for trace in range(7):
            newSample = 0
            for sample in range(5):
                for i in range(2):
                    TRAINOFFSET = (1/3)*10*1000*1000*1000#+-3.333 seconds offset
                    if i == 0:
                        TRAINOFFSET*=-1
                        
                    TESTOFFSET = 0

                    if folder >= 10:
                        filename = "dataset-231011-last2min/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        if newSample >= 10:
                            f = open("offset-train/k2size5/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                        else:
                            f = open("offset-train/k2size5/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                    else:
                        filename = "dataset-231011-last2min/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        if newSample >= 10:
                            f = open("offset-train/k2size5/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                        else:
                            f = open("offset-train/k2size5/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                    newSample += 1
                    file = open(filename)
                    file_str = file.read()
                    s = file_str.split("\n")
                    for line in s:
                        offset = 10*1000000000
                        parts = line.split(",")
                        if len(parts) < 3:
                            continue

                        if trace == 6:
                            #testoffset
                            offset += TESTOFFSET
                        else:
                            #testoffset
                            offset += TRAINOFFSET
                        
                        if float(parts[0]) < offset:
                            continue

                        time = float(parts[0]) - offset

                        if time > 100 * 1000000000: #100second long trace 
                            break

                        f.write(str(time))
                        f.write(",")
                        f.write(str(parts[1]))
                        f.write(",")
                        f.write(str(parts[2]))
                        f.write(",")
                        f.write(str(parts[3]))
                        f.write("\n")

def offset_train_dataset_last2min_k3():
    print("k3")
    for folder in range(100):
        print(folder)
        os.mkdir("offset-train/k3size5/"+str(folder))
        for trace in range(7):
            newSample = 0
            for sample in range(5):
                for i in range(4):
                    TRAINOFFSET = (-6+(4*i))*1000*1000*1000
                        
                    TESTOFFSET = 0#-9*1000000000 + 2*i*1000000000 #-9,-7,-5,-3,-1,1,3,5,7,9

                    if folder >= 10:
                        filename = "dataset-231011-last2min/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        if newSample >= 10:
                            f = open("offset-train/k3size5/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                        else:
                            f = open("offset-train/k3size5/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                    else:
                        filename = "dataset-231011-last2min/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        if newSample >= 10:
                            f = open("offset-train/k3size5/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                        else:
                            f = open("offset-train/k3size5/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                    newSample += 1
                    file = open(filename)
                    file_str = file.read()
                    s = file_str.split("\n")
                    for line in s:
                        offset = 10*1000000000
                        parts = line.split(",")
                        if len(parts) < 3:
                            continue

                        if trace == 6:
                            #testoffset
                            offset += TESTOFFSET
                        else:
                            #testoffset
                            offset += TRAINOFFSET
                        
                        if float(parts[0]) < offset:
                            continue

                        time = float(parts[0]) - offset

                        if time > 100 * 1000000000: #100second long trace 
                            break

                        f.write(str(time))
                        f.write(",")
                        f.write(str(parts[1]))
                        f.write(",")
                        f.write(str(parts[2]))
                        f.write(",")
                        f.write(str(parts[3]))
                        f.write("\n")

def offset_train_dataset_last2min_k4():
    print("k4")
    for folder in range(100):
        print(folder)
        os.mkdir("offset-train/k42min/"+str(folder))
        for trace in range(9):
            newSample = 0
            for sample in range(10):
                for i in range(8):
                    INCREMENT = 10/9
                    TRAINOFFSET = ((-7*INCREMENT)+(2*i*INCREMENT))*1000*1000*1000

                    TESTOFFSET = 0#-9*1000000000 + 2*i*1000000000 #-9,-7,-5,-3,-1,1,3,5,7,9

                    if folder >= 10:
                        filename = "dataset-231121-last2min/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        if newSample >= 10:
                            f = open("offset-train/k42min/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                        else:
                            f = open("offset-train/k42min/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                    else:
                        filename = "dataset-231121-last2min/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        if newSample >= 10:
                            f = open("offset-train/k42min/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                        else:
                            f = open("offset-train/k42min/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                    newSample += 1
                    file = open(filename)
                    file_str = file.read()
                    s = file_str.split("\n")
                    for line in s:
                        offset = 10*1000*1000*1000
                        parts = line.split(",")
                        if len(parts) < 3:
                            continue

                        if trace == 8:
                            #testoffset
                            offset += TESTOFFSET
                        else:
                            #testoffset
                            offset += TRAINOFFSET
                        
                        if float(parts[0]) < offset:
                            continue

                        time = float(parts[0]) - offset

                        if time > 100 * 1000000000: #100second long trace 
                            break

                        f.write(str(time))
                        f.write(",")
                        f.write(str(parts[1]))
                        f.write(",")
                        f.write(str(parts[2]))
                        f.write(",")
                        f.write(str(parts[3]))
                        f.write("\n")

def offset_train_dataset_last1min_k4():
    print("k4")
    for folder in range(100):
        print(folder)
        os.mkdir("offset-train/k41min/"+str(folder))
        for trace in range(10):
            newSample = 0
            for sample in range(10):
                for i in range(8):
                    INCREMENT = 10/9
                    TRAINOFFSET = ((-7*INCREMENT)+(2*i*INCREMENT))*1000*1000*1000

                    TESTOFFSET = 0#-9*1000000000 + 2*i*1000000000 #-9,-7,-5,-3,-1,1,3,5,7,9

                    if folder >= 10:
                        filename = "dataset-231121-last1min/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        if newSample >= 10:
                            f = open("offset-train/k41min/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                        else:
                            f = open("offset-train/k41min/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                    else:
                        filename = "dataset-231121-last1min/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        if newSample >= 10:
                            f = open("offset-train/k41min/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                        else:
                            f = open("offset-train/k41min/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                    newSample += 1
                    file = open(filename)
                    file_str = file.read()
                    s = file_str.split("\n")
                    for line in s:
                        offset = 10*1000000000
                        parts = line.split(",")
                        if len(parts) < 3:
                            continue

                        if trace == 9:
                            #testoffset
                            offset += TESTOFFSET
                        else:
                            #testoffset
                            offset += TRAINOFFSET
                        
                        if float(parts[0]) < offset:
                            continue

                        time = float(parts[0]) - offset

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

def offset_train_dataset_60s_k4():
    print("k4")
    for folder in range(100):
        print(folder)
        os.mkdir("offset-train/k4-60s/"+str(folder))
        for trace in range(9):
            newSample = 0
            for sample in range(10):
                for i in range(8):
                    INCREMENT = 10/9
                    TRAINOFFSET = ((-7*INCREMENT)+(2*i*INCREMENT))*1000*1000*1000

                    TESTOFFSET = 0#-9*1000000000 + 2*i*1000000000 #-9,-7,-5,-3,-1,1,3,5,7,9

                    if folder >= 10:
                        filename = "dataset-231121-last2min/none/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        if newSample >= 10:
                            f = open("offset-train/k4-60s/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                        else:
                            f = open("offset-train/k4-60s/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                    else:
                        filename = "dataset-231121-last2min/none/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        if newSample >= 10:
                            f = open("offset-train/k4-60s/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                        else:
                            f = open("offset-train/k4-60s/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                    newSample += 1
                    file = open(filename)
                    file_str = file.read()
                    s = file_str.split("\n")
                    for line in s:
                        offset = 10*1000000000
                        parts = line.split(",")
                        if len(parts) < 3:
                            continue

                        if trace == 8:
                            #testoffset
                            offset += TESTOFFSET
                        else:
                            #testoffset
                            offset += TRAINOFFSET
                        
                        if float(parts[0]) < offset:
                            continue

                        time = float(parts[0]) - offset

                        if time > 60 * 1000000000: #100second long trace 
                            break

                        f.write(str(time))
                        f.write(",")
                        f.write(str(parts[1]))
                        f.write(",")
                        f.write(str(parts[2]))
                        f.write(",")
                        f.write(str(parts[3]))
                        f.write("\n")

def offset_train_dataset_last2min_k1_fair():
    for folder in range(100):
        print(folder)
        os.mkdir("offset-train/k1fair/"+str(folder))
        for trace in range(7):
            newSample = 0
            for sample in range(7):#7,14,28
                for i in range(8):#8,4,2
                    if folder >= 10:
                        filename = "offset-train/k1/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        if newSample >= 10:
                            f = open("offset-train/k1fair/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                        else:
                            f = open("offset-train/k1fair/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                    else:
                        filename = "offset-train/k1/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                        if newSample >= 10:
                            f = open("offset-train/k1fair/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                        else:
                            f = open("offset-train/k1fair/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")

                    newSample += 1
                    file = open(filename)
                    file_str = file.read()
                    s = file_str.split("\n")
                    for line in s:
                        parts = line.split(",")
                        if len(parts) < 3:
                            continue

                        f.write(str(parts[0]))
                        f.write(",")
                        f.write(str(parts[1]))
                        f.write(",")
                        f.write(str(parts[2]))
                        f.write(",")
                        f.write(str(parts[3]))
                        f.write("\n")

def offset_train_dataset_last2min_k2_fair():
    for folder in range(100):
        print(folder)
        os.mkdir("offset-train/k2fair/"+str(folder))
        for trace in range(7):
            newSample = 0
            for sample in range(14):#7,14,28
                for i in range(4):#8,4,2
                    if folder >= 10:
                        if sample >= 10:
                            filename = "offset-train/k2/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-00"+str(sample)+".log"
                            if newSample >= 10:
                                f = open("offset-train/k2fair/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                            else:
                                f = open("offset-train/k2fair/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                        else: 
                            filename = "offset-train/k2/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                            if newSample >= 10:
                                f = open("offset-train/k2fair/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                            else:
                                f = open("offset-train/k2fair/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                    else:
                        if sample >= 10:
                            filename = "offset-train/k2/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-00"+str(sample)+".log"
                            if newSample >= 10:
                                f = open("offset-train/k2fair/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                            else:
                                f = open("offset-train/k2fair/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                        else:
                            filename = "offset-train/k2/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                            if newSample >= 10:
                                f = open("offset-train/k2fair/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                            else:
                                f = open("offset-train/k2fair/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                        
                    newSample += 1
                    file = open(filename)
                    file_str = file.read()
                    s = file_str.split("\n")
                    for line in s:
                        parts = line.split(",")
                        if len(parts) < 3:
                            continue

                        f.write(str(parts[0]))
                        f.write(",")
                        f.write(str(parts[1]))
                        f.write(",")
                        f.write(str(parts[2]))
                        f.write(",")
                        f.write(str(parts[3]))
                        f.write("\n")

def offset_train_dataset_last2min_k3_fair():
    for folder in range(100):
        print(folder)
        os.mkdir("offset-train/k3fair/"+str(folder))
        for trace in range(7):
            newSample = 0
            for sample in range(28):#7,14,28
                for i in range(2):#8,4,2
                    if folder >= 10:
                        if sample >= 10:
                            filename = "offset-train/k3/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-00"+str(sample)+".log"
                            if newSample >= 10:
                                f = open("offset-train/k3fair/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                            else:
                                f = open("offset-train/k3fair/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                        else: 
                            filename = "offset-train/k3/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                            if newSample >= 10:
                                f = open("offset-train/k3fair/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                            else:
                                f = open("offset-train/k3fair/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                    else:
                        if sample >= 10:
                            filename = "offset-train/k3/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-00"+str(sample)+".log"
                            if newSample >= 10:
                                f = open("offset-train/k3fair/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                            else:
                                f = open("offset-train/k3fair/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                        else:
                            filename = "offset-train/k3/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".log"
                            if newSample >= 10:
                                f = open("offset-train/k3fair/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-00"+str(newSample)+".log", "w+")
                            else:
                                f = open("offset-train/k3fair/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(newSample)+".log", "w+")
                        

                    newSample += 1
                    file = open(filename)
                    file_str = file.read()
                    s = file_str.split("\n")
                    for line in s:
                        parts = line.split(",")
                        if len(parts) < 3:
                            continue

                        f.write(str(parts[0]))
                        f.write(",")
                        f.write(str(parts[1]))
                        f.write(",")
                        f.write(str(parts[2]))
                        f.write(",")
                        f.write(str(parts[3]))
                        f.write("\n")

#offset_train_dataset_last2min_k4()
#offset_train_dataset_last2min_k3()
#datasetx6()
#offset_all_dataset_last2min()
#offset_test_dataset_last2min()
#offset_test_dataset_last1min()
#offset_dataset_split()
#offset_dataset()
#merge_datasets()
#delete_png()
#format_RF()
#last2min()
#last1min()
#ten_seconds()
#offset_train_dataset_last2min_k1()
#offset_train_dataset_last1min_k4()
#offset_train_dataset_last2min_k4()
offset_train_dataset_last2min_k4()
