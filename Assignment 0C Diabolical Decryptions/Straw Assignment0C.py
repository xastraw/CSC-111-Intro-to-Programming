
from StrawEncryptionLibrary import *
import time

dictionarytext = open("dictionary.txt", "r")
outputtext = open("decrypted.txt", "w")

keytext = open("dictionary.txt", "r")
vigenereOutput = open("vigenereDecrypt.txt", "w")
#the results for vigenere decryption are on the vigenere decryption SAVE doc, so dont have to wait the full thing

message1 = "IZIVCFSHCPSZIWFCVSR"
message2 = "CWFIUHXPQYJUWLJQPVP"
message3 = "OTWWOWRZUIMIPZLUXPVVW"


def decodeCaesar():
    for i in range(0,26):
        print("Key: ", i, "\t", CaesarDecrypt(message1, i))
    
    #made the results variables so u dont have to run it through again
    caseardec = "EVERYBODYLOVESBYRON"
    casearshi = 4
    outputtext.write("The decrypted cipher message is: " + caseardec + " and the key is: " + str(casearshi))


def decodedEvilCaesar():
    
    for i in range(0,26):
        for r in range(0,26):
            print("Key1: ", i, "\tKey2: ", r, "\t", EvilCaesarDecrypt(message2, i, r))
    
    #made the results variables so u dont have to run it through again
    evilCaesardec = "LEMOZLARRYISTHEKING"
    evilCaeSh1 = 3
    evilCaeSh2 = 14
    outputtext.write("\nThe decrypted evil cipher message is " + evilCaesardec + " and the first key is: " + str(evilCaeSh1) + " and the second key is: " + str(evilCaeSh2))


def decodeVign():

    startTime = time.time() #time started

    diction = []
    wordlist = []
    countCases = 0

    for lines in dictionarytext:
        #list of dictionary words to use as keys
        thisline = lines.split()
        for words in thisline:
            diction.append(words)

    for line in keytext:
        #creating another list of all words to see if those words are inside of any of the decrypeted keys
        currentline = line.split()
        for word in currentline:
            if len(word) > 4 and len(word) < 9:
                #making the words between 5 and 8 characters to limit down the amount of words I have to check for
                #also doing this b/c the chance that 2 or 3 letter words happen to be in a decoded message by pure chance is alot higher
                wordlist.append(word)

    print("\nSet doVigenere to true if you want to run through the vigenere decryption again (it takes nearly 4 hours....)")
    doVigenere = False

    if doVigenere == True:
        for i in range (len(diction)):
            #this tests every key
            trykey = diction[i]
            for k in range ((len(wordlist))):
                if wordlist[k] in VigenereDecrypt(message3, trykey):
                    vigenereOutput.write("The key is: " + trykey + "\t\t\t\t Decoded message: " + VigenereDecrypt(message3, trykey) + "\n")
                    countCases+=1
        

        stopTime = time.time() #time ended
        totalTime = stopTime - startTime    #takes time ended minus time started
        timer(totalTime)    #calculates how long the entire program took

        vigenereOutput.write("\n")
        vigenereOutput.write("\nThere are " + str(countCases) + " occurences") 
        #writing to seperate doc so i can keep the decrypted doc mainly clean
        #using countcases to see how many results there are


    vignKey = "Split"
    vignMsg = "WELOVECOMPUTERSCIENCE"

    outputtext.write("\nThe decrypted vigenere cipher is: " + vignMsg + " and the key is: " + vignKey)


def timer(sec):
    #using this too make a simple timer to see how long decoding the vigenere cipher takes
    mins = sec//60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60

    vigenereOutput.write("\n\n")
    vigenereOutput.write("Time Elapsed: \tHours: " + str(hours) + "\t Mins: "+ str(mins) + "\t Seconds: "+ str(round(sec, 2)))


def main():
    decodeCaesar()
    decodedEvilCaesar()
    decodeVign()


main()

keytext.close()
dictionarytext.close()
vigenereOutput.close()
outputtext.close()