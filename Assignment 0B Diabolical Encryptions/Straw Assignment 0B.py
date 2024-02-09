
from StrawEncryptionLibrary import *

#-------------------------------
#           READ
#   You must move the StrawEncryptionLibrary.py doc over to the folder Straw Assignmetn 0B for this to work
#
#--------------------------
caesartext = open("caesar.txt", "r")
caesarRead = []
evilcaesartext = open("evilcaesar.txt", "r")
evilCaesarRead = []
vigeneretext = open("vigenere.txt", "r")
vigenereRead = []



def checkCaesar():

    for line in caesartext:             #makes the doc into something python can read
        thisline = line.split()
        for word in thisline:
            caesarRead.append(word.split(","))


    for i in range(len(caesarRead)):
        caesarinp, caesarshi, caesarEnc = caesarRead[i]
        caesarshi = int(caesarshi)  #is reading the shift as a string so set it to and int
        
        #print("Caesar input: \t\t", caesarinp)
        #print("Shift amount: \t\t", caesarshi)
        #print("Should be: \t\t", caesarEnc)

        #print("Caesar Encryption: \t", CaesarEncrypt(caesarinp, caesarshi))

            
        assert(CaesarEncrypt(caesarinp, caesarshi) == caesarEnc), "caesar encrypt"
        assert(CaesarDecrypt(caesarEnc, caesarshi) == caesarinp), "caesar decrypt"

def checkEvilCaesar():

    for line in evilcaesartext:             #makes the doc into something python can read
        thisline = line.split()
        for word in thisline:
            evilCaesarRead.append(word.split(","))
    
    for i in range(len(evilCaesarRead)):
        evilCaeinp, evilCaeShift1, evilCaeShift2, evilCaeDec = evilCaesarRead[0]
        evilCaeShift1 = int(evilCaeShift1)  #change values from str to int
        evilCaeShift2 = int(evilCaeShift2)

        assert(EvilCaesarEncrypt(evilCaeinp, evilCaeShift1, evilCaeShift2) == evilCaeDec), "evil casear encrypt"
        assert(EvilCaesarDecrypt(evilCaeDec, evilCaeShift1, evilCaeShift2) == evilCaeinp), "evil caesar decrypt"

def checkVigenere():

    for line in vigeneretext:             #makes the doc into something python can read
        thisline = line.split()
        for word in thisline:
            vigenereRead.append(word.split(","))
    
    for i in range(len(vigenereRead)):
        vinInp, vinKey, vinDec = vigenereRead[0]

        assert(VigenereEncrypt(vinInp, vinKey) == vinDec), "vigenere encrypt"
        assert(VigenereDecrypt(vinDec, vinKey) == vinInp), "Vigenere decrypt"



def main():
    checkCaesar()
    checkEvilCaesar()
    checkVigenere()



main()

caesartext.close()
evilcaesartext.close()
vigeneretext.close()