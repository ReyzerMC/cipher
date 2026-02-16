#!/bin/python3
import os
import questionary
from nacl.secret import SecretBox
from config import VERSION, KEY_DIR, SENSITIVE_DIRS, dirs
from utils import printTree, antiSily, isSensitive, generateKey

def startEnc():
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
    checker(response, 1)

def startDec():
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

def checker(path, EnOrDe):
    if os.path.exists(KEY_DIR):
        with open(KEY_DIR, "rb") as f:
            key = f.read()
    else:
        key = generateKey()

    isSensitive(path)

    if os.path.isdir(path):
        printTree(path)
        antiSily()
        for root, dirs, files in os.walk(path):
            for name in files:
                fullPath = os.path.join(root, name)
                if os.path.isfile(fullPath):
                    if EnOrDe == 1:
                        encryptFile(fullPath, key)
                    elif EnOrDe == 0:
                        decriptFile(fullPath, key)
    elif os.path.isfile(path):
        if EnOrDe == 1:
            encryptFile(path, key)
        elif EnOrDe == 0:
            decriptFile(path, key)

def encryptFile(fileName, key):
    box = SecretBox(key)
    if fileName.endswith(".cph"):
        pass
    else:
        with open(fileName, "rb") as f:
            data = f.read()

        encrypted = box.encrypt(data)

        with open(fileName + ".cph", "wb") as f:
            f.write(encrypted)
        os.remove(fileName)

def decriptFile(fileName, key):
    box = SecretBox(key)
    if fileName.endswith(".cph"):
        with open(fileName, "rb") as f:
            cphData = f.read()

        decripted = box.decrypt(cphData)
        originalName = fileName.replace(".cph", "")

        with open(originalName, "wb") as f:
            f.write(decripted)
        os.remove(fileName)
    else:
        pass

if __name__ == "__main__":
    dirs()
    option = questionary.select(
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