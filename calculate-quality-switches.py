


PATH="../../data/dataset-var/none-none-bw4"

def read_quality():
    qualitySwitches = []
    allQualities = []
    for folder in range(100):
        print(folder)
        for trace in range(10):
            for sample in range(10):
                if folder >= 10:
                    filename = PATH+"/"+str(folder)+"/00"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".qoe.log"
                else:
                    filename = PATH+"/"+str(folder)+"/000"+str(folder)+"-000"+str(trace)+"-000"+str(sample)+".qoe.log"

                file = open(filename)
                file_str = file.read()
                s = file_str.split("\n")
                qualities = []
                qualityNextLine = False
                quality = 2000
                for line in s:
                    parts = line.split(",")

                    if len(parts) < 2:
                        continue

                    if qualityNextLine:
                        quality = float(parts[2])
                        qualityNextLine = False

                    if parts[1] == "qualityChangeRequested":
                        qualityNextLine = True

                    if parts[1] == "qualityChangeRendered":
                        if qualities:
                            if qualities[-1] != quality:
                                qualities.append(quality)
                        else:
                            qualities.append(quality)

                allQualities.append(qualities)
                qualitySwitches.append(len(qualities))

    print("Results:")
    total = 0
    for switches in qualitySwitches:
        total+=switches
    print(total)

    from1to2 = 0
    from1to4 = 0
    from2to1 = 0
    from2to4 = 0
    from4to1 = 0
    from4to2 = 0

    for sampleQualites in allQualities:
        previousQuality = 0
        for sampleQuality in sampleQualites:
            saveQuality = sampleQuality
            sampleQuality = int((sampleQuality+200)/1000)
            if previousQuality == 0:
                previousQuality = sampleQuality
            elif previousQuality == 1:
                if sampleQuality == 2:
                    from1to2 += 1
                elif sampleQuality == 4:
                    from1to4 += 1
                else:
                    print(saveQuality, "a", previousQuality)
            elif previousQuality == 2:
                if sampleQuality == 1:
                    from2to1 += 1
                elif sampleQuality == 4:
                    from2to4 += 1
                else:
                    print(saveQuality, "b", previousQuality)
            elif previousQuality == 4:
                if sampleQuality == 1:
                    from4to1 += 1
                elif sampleQuality == 2:
                    from4to2 += 1
                else:
                    print(saveQuality, "c", previousQuality)
            else:
                print(saveQuality, "d", previousQuality)
            previousQuality = sampleQuality

    print("1to2", from1to2)
    print("1to4", from1to4)
    print("2to1", from2to1)
    print("2to4", from2to4)
    print("4to1", from4to1)
    print("4to2", from4to2)


read_quality()
