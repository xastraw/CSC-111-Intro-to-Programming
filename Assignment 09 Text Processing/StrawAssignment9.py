
inputtext = open("input.txt", "r")
outputtext = open("output.txt", "w")


wordList = []
nodupelist = []


def cntWords():
    #counts words and lines
    numberoflines = 0

    for lines in inputtext:
        individuallines = lines.split()
        numberoflines = numberoflines + 1
        for word in individuallines:
            word = word.replace(",", "")
            word = word.replace(";", "")
            word = word.replace(".", "")
            word = word.replace("!", "")
            word = word.replace(":", "")
            word = word.replace("?", "")
            word = word.replace("(", "")
            word = word.replace(")", "")
            word = word.replace("'", "")
            wordList.append(word)
    outputtext.write("Number of lines: " + str(numberoflines) + "\n")
    outputtext.write("number of words: " + str(len(wordList)) + "\n")


def wordCntdupe():
    #makes a word count taking away any dupes
    for word in wordList:
        if word not in nodupelist:
            nodupelist.append(word)
    outputtext.write("Word count without duplicates: " + str(len(nodupelist)) + "\n")


def azChr():
    #gets a-z character list
    azchar = 0
    for word in wordList:
        azchar = azchar + len(word)
    outputtext.write("Number of alphabetic characters: " + str(azchar) + "\n")


def allChr():
    #gets number of all characters
    tempdoc = open("input.txt", "r")
    text = tempdoc.read()
    numchar = len(text)
    outputtext.write("Number of total characters: " + str(numchar) + "\n")
   
def main():
    cntWords()
    wordCntdupe()
    azChr()
    allChr()

main()

inputtext.close()
outputtext.close()