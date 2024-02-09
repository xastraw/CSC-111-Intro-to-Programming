
def CaesarEncrypt(plainstring, shift):
    message = ""
    for i in range(len(plainstring)):
        letter = chr(((ord(plainstring[i]) - 65 + shift) % 26) + 65)
        message = message + letter
    
    return message


def CaesarDecrypt(encryptedstring, shift): 
    message = CaesarEncrypt(encryptedstring, -shift)
    return message


def EvilCaesarEncrypt(plainstring, shift1, shift2):
    #shift1 is the starting amount of shift or the base shift
    #shift2 is the amount added to the base shift 
    message = "" 
    for i in range(len(plainstring)):
        letter = chr(((ord(plainstring[i]) - 65 + shift1 + shift2) % 26) + 65)
        message = message + letter
        shift2 = shift2 +1
    return message


def EvilCaesarDecrypt(encryptedstring, shift1, shift2):
    message = ""
    for i in range(len(encryptedstring)):
        letter = chr(((ord(encryptedstring[i]) - 65 - shift1 - shift2) % 26) + 65)
        message = message + letter
        shift2 = shift2 +1
    return message


def VigenereEncrypt(plainstring, key):
    message = ""
    for i in range(len(plainstring)):
        letter = chr((((ord(key[i])-65) + (ord(plainstring[i])-65)) % 26)+65)   #adds the 0-25 value of both characters together to get the correctkey
        message = message + letter
        if len(plainstring) > len(key):     #fixes the problem where the loop would crash if the key was shorter than the input string
            key = key + key[i]
    return message


def VigenereDecrypt(encryptedstring, key):
    message = ""
    for i in range(len(encryptedstring)):
        letter = chr((((ord(encryptedstring[i])-65) - (ord(key[i])-65)) % 26)+65)   #subtracts the 0-25 value of the key from the encrypted string
        message = message + letter
        if len(encryptedstring) > len(key):     #fixes the problem where the loop would crash if the key was shorter than the input string
            key = key + key[i]
    return message
