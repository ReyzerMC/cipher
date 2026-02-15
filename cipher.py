#!/bin/python3
import os
import questionary
import nacl.utils
import sys
from nacl.secret import SecretBox
from config import VERSION, KEY_DIR, SENSITIVE_DIRS, dirs

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

def antiSily():
    r = input(f"!! Are you sure you want to perform this action for this entry? [y/N]: ")
    if r.lower() == "y":
        pass
    else:
        print("Operation cancelled. Exiting.", file=sys.stderr)
        sys.exit(1)

def printTree(path, prefix=""):
    print(prefix + os.path.basename(path) + "/")
    if os.path.isdir(path):
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                printTree(full_path, prefix + "│   ")
            else:
                print(prefix + "│   " + item)

def isSensitive(path):
    abs_path = os.path.abspath(path)
    for s in SENSITIVE_DIRS:
        if abs_path.startswith(os.path.abspath(s)):
            warn = input(f"!! Sensitive directory detected: {abs_path}\nAre you sure? [y/N]: ")
            if warn.lower() != "y":
                print("Operation cancelled. Exiting.", file=sys.stderr)
                sys.exit(1)
            break  # solo preguntar una vez

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

def generateKey():
    key = nacl.utils.random(SecretBox.KEY_SIZE)
    with open(KEY_DIR, "wb") as keyFile:
        keyFile.write(key)
    return key

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
