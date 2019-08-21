textFile = open("txt.txt", "r")
wordSum = 0
lineCount = 0
charCount = 0
for line in textFile:
    wordSum += len(line.split())
    lineCount += 1
    for word in line:
        word = word.strip(".").strip(")").strip("(") .strip("!") .strip(",") .strip(";") .strip("-")        
        charCount += len(word)
        
print("The average number of words per sentence is:", round(wordSum/lineCount))
print("The average number of characters per word is:", round(charCount/wordSum))
textFile.close()