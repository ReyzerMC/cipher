import sys
import os
import nacl.utils
from nacl.secret import SecretBox
from config import SENSITIVE_DIRS, KEY_DIR

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

def generateKey():
    key = nacl.utils.random(SecretBox.KEY_SIZE)
    with open(KEY_DIR, "wb") as keyFile:
        keyFile.write(key)
    return key