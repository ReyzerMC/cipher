import os
import uuid

VERSION = "1.0.0" # Actual cipher version
_KEY_ID = 0 # Key ID initialization
CONFIG_DIR = os.path.expanduser("~/.config/cipher") # Config DIR
KEY_PATH = os.path.join(CONFIG_DIR, "key") # Key path in the config DIR
KEY_DIR = os.path.join(KEY_PATH, f"{_KEY_ID}.key") # Key DIR in the config
SENSITIVE_DIRS = [ # Sensitive dirs to avoid accidentally ecnrypting something sensitive like config dirs and user files (.local, .config)
    os.path.expanduser("~/.config"), os.path.expanduser("~/.var"),
    os.path.expanduser("~/.cache"), os.path.expanduser("~/.local"),
    os.path.expanduser("~/.firefox"), os.path.expanduser("~/.mozilla"),
    os.path.expanduser("~/.gnupg"), os.path.expanduser("~/.ssh"),
    os.path.expanduser("~/.npm"), os.path.expanduser("~/.yarn"),
    os.path.expanduser("~/.python"), os.path.expanduser("~/.thunderbird")
]

def dirs(): # Main function to create config dirs (Key dir) and generates the key path with generateID() function
    global _KEY_ID, KEY_DIR # Globalizing variables
    if not os.path.exists(CONFIG_DIR): # If not exists check
        os.makedirs(CONFIG_DIR, exist_ok=True)

    if not os.path.exists(KEY_PATH): # Same check but for key path
        os.makedirs(KEY_PATH, exist_ok=True)

    if not os.path.exists(KEY_DIR): # Same check but for generate the key
        _KEY_ID = generateID() # ID generation
        KEY_DIR = os.path.join(KEY_PATH, f"{_KEY_ID}.key")

def generateID(): # Function to generate de ID
    return uuid.uuid4().int
