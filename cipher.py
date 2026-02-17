#!/bin/python3
import os
import questionary
from nacl.secret import SecretBox
from config import VERSION, KEY_DIR, dirs
from utils import printTree, antiSily, isSensitive, generateKey

def startEnc(): # Encription startup
    cwd = os.getcwd() # Gets actual work directory
    cwdDirs = []
    for entry in os.listdir(cwd): # Get a list of all the dirs inside the actual work directory
        fullpath = os.path.join(cwd, entry)
        cwdDirs.append(fullpath)

    response = questionary.select( # Questionary for selecting dir to encript
        "",
        choices=cwdDirs,
        pointer='->'
    ).ask()
    checker(response, 1) # Calls the function checher() with a 1 to Encrypt

def startDec(): # Decription startup (Im not documenting this cause is the same that the above funtion only changes that this one gives a 0 to checher() for decription)
    cwd = os.getcwd()
    cwdDirs = []
    for entry in os.listdir(cwd):
        fullpath = os.path.join(cwd, entry)
        cwdDirs.append(fullpath)

    response = questionary.select(
        "",
        choices=cwdDirs,
        pointer='->'
    ).ask()
    checker(response, 0)

# Function that checks -> if folders, files, etc... | Security checks antiSilly(), isSensitive() | And info printTree()

def checker(path, EnOrDe):
    if os.path.exists(KEY_DIR): # Checks if exists a key file in teh actual sistem ~/.config/cipher/key/cph.key
        with open(KEY_DIR, "rb") as f:
            key = f.read()
    else:
        key = generateKey() # Generates a key if not

    isSensitive(path) # Checks if the path contains sensitive directories and warns the user

    if os.path.isdir(path): # Easy ->> if folder or file
        printTree(path) # Dir in tree
        antiSily() # AntiSilys function to prevent data loss
        for root, dirs, files in os.walk(path): # Navigate the directory (subFolders & files)
            for name in files:
                fullPath = os.path.join(root, name) # Gets the full path for each file / folder
                if os.path.isfile(fullPath): 
                    if EnOrDe == 1: # Selector of Decript or Encript (depends on what function calls this one)
                        encryptFile(fullPath, key)
                    elif EnOrDe == 0:
                        decriptFile(fullPath, key)
    elif os.path.isfile(path): # This is for single files
        if EnOrDe == 1: # Same selector
            encryptFile(path, key)
        elif EnOrDe == 0:
            decriptFile(path, key)

def encryptFile(fileName, key): # Method to encrypt files
    box = SecretBox(key)
    if fileName.endswith(".cph"): # Checks if not .cph files there
        pass
    else:
        with open(fileName, "rb") as f: # Opens current file and reads it
            data = f.read()
        encrypted = box.encrypt(data) # Encrypts data

        with open(fileName + ".cph", "wb") as f: # Opens a new file to write the encrypted data
            f.write(encrypted)
        os.remove(fileName) # Removes original file to leave only .cph version (Encrypted version)

def decriptFile(fileName, key): # Decrypt function
    box = SecretBox(key)
    if fileName.endswith(".cph"): # Checks if is a .cph file
        with open(fileName, "rb") as f: # Opens current .cph file and reads its content
            cphData = f.read()

        decripted = box.decrypt(cphData) # Decrypt data
        originalName = fileName.replace(".cph", "") # Remove .cph extension to leave the original name of the file

        with open(originalName, "wb") as f: # Opens a new file with the original name and wirtes the decyipted data in it
            f.write(decripted)
        os.remove(fileName) # Removes encrypted version
    else:
        pass

if __name__ == "__main__": # Entry point
    dirs() # Calls a function to create the needed dirs
    option = questionary.select( # Main questionary to choose Encrypt or Decrypt
        f"Cipher encryptor --- v{VERSION}", 
        choices=[
            "Encrypt",
            "Decrypt"
            ],
        pointer='->'
    ).ask()
    if option == "Encrypt":
        startEnc()
    elif option == "Decrypt":
        startDec()
