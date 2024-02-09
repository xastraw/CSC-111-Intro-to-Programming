

inputtext = open("input.txt", "r")
outputtext = open("output.txt", "w")


dict = {
'yes':	'aye',
'no':	'nay',
'bathroom': 'head',
'restroom': 'head',
'professor':	'foul blaggart',
'madam':	'proud beauty',
'woman': 'proud beauty',
'girl': 'proud beauty',
'boy':	'matey',
'sir':	'matey',
'man':	'matey',
'dude':	'matey',
'restaurant':	'galley',
'Sparks':	'galley',
'student':	'swabby',
'students':	'swabbies',
'hotel':	'fleabag inn',
'dorm':	'fleabag inn',
'frat':	'fleabag inn',
'food': 'crum',
'room': 'quarters',
}

listofwords = []

for line in inputtext:      #makes the list
    linesofwords = line.split()
    for word in linesofwords:
        listofwords.append(word)


tempnum = 10    #just using this to break the lines and make the paragraph easier to read on notepad
for i in range(len(listofwords)):
    word = listofwords[i]
    
    if i == tempnum:
        outputtext.write("\n")
        tempnum = tempnum +10
    if word in dict:
        value = dict[word]
        outputtext.write(value + " ")
    else:
        outputtext.write(word + " ")



inputtext.close()
outputtext.close()

