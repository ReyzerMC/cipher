import sys
import os
import nacl.utils
from nacl.secret import SecretBox
from config import SENSITIVE_DIRS, KEY_DIR

def antiSily(): # Function to avoid accidentally encrypt something
    r = input(f"!! Are you sure you want to perform this action for this entry? [y/N]: ") # Mini check to avoid it
    if r.lower() == "y":
        pass # Continue in case of Y
    else:
        print("Operation cancelled. Exiting.", file=sys.stderr) # Error with sys.stderr if you select N
        sys.exit(1)

def printTree(path, prefix=""): # Auxiliar function to print the tree of what are you encrypting
    print(prefix + os.path.basename(path) + "/")
    if os.path.isdir(path): # Verification if is a dir
        for item in os.listdir(path): # List dirs
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path): # Build the tree
                printTree(full_path, prefix + "│   ")
            else:
                print(prefix + "│   " + item)

def isSensitive(path): # Funtion to chech if a path contains sensitive dirs
    abs_path = os.path.abspath(path) # Get the absolute path
    for s in SENSITIVE_DIRS: # Check every dir in the path, if contains a sensitive dir
        if abs_path.startswith(os.path.abspath(s)):
            warn = input(f"!! Sensitive directory detected: {abs_path}\nAre you sure? [y/N]: ") # Question if you know what are you doing
            if warn.lower() != "y":
                print("Operation cancelled. Exiting.", file=sys.stderr)
                sys.exit(1)
            break # This is serious, you will only be asked once.

def generateKey(): # Generates the key that is stored at ~/.config/cipher/key/'ID'.key
    key = nacl.utils.random(SecretBox.KEY_SIZE)
    with open(KEY_DIR, "wb") as keyFile:
        keyFile.write(key)
    return key