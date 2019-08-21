textFile = open("txt.txt", "r")
recordDict = {}
reportFile = open("report.txt", "w")
for line in textFile:
    wordList = line.split()

    for word in wordList:
        word = word.strip(".")
        word = word.strip(")")
        word = word.strip("(")
        word = word.strip("!")
        word = word.strip(",")
        word = word.strip(";")
        word = word.strip("-")
        word = word.lower()
        if recordDict.get(word,False) == False:
            recordDict[word] = 1
        else:
            recordDict[word] += 1
for item in recordDict:
    reportFile.write(item + ": " + str(recordDict.get(item)) + "\n")

textFile.close()
reportFile.close()