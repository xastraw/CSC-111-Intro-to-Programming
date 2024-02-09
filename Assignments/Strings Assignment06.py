import random

def upperCase(string):
    
    upperString = ""
    for i in range(len(string)):
        if(string[i] >= 'a') and (string[i] <= 'z'):    #if letter is lowercase uppercase it
            upperString = upperString + chr(ord(string[i])-32)
        else:
            upperString = upperString + string[i]           #if letter is uppercase dont do anything (alr uppercase)
    return upperString


def lowerCase(string):

    lowerString = ""
    for i in range(len(string)):
        if(string[i] >= 'A') and (string[i] <= 'Z'):        #if letter is uppercase lowercase it
            lowerString = lowerString + chr(ord(string[i])+32)
        else:
            lowerString = lowerString + string[i]           #if letter is lowercase dont do anything (alr lowercase)
    return lowerString

def spongeBob(thestring):

    newWord = ""

    for u in range(len(thestring)):

        numberGen = random.randint(0, 10)

        if numberGen % 2 == 0:      #lowercase
            newWord = newWord + lowerCase(thestring[u])
        else:               #uppercase
            newWord =  newWord + upperCase(thestring[u])
    return newWord

def main():

    word = str(input("What do you want to Spongebob-ify? "))
    print(word)
    print(spongeBob(word))


main()