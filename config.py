import os
import uuid

VERSION = "1.0.0"
_KEY_ID = 0
CONFIG_DIR = os.path.expanduser("~/.config/cipher")
KEY_PATH = os.path.join(CONFIG_DIR, "key")
KEY_DIR = os.path.join(KEY_PATH, f"{_KEY_ID}.key")
SENSITIVE_DIRS = [
    os.path.expanduser("~/.config"), os.path.expanduser("~/.var"),
    os.path.expanduser("~/.cache"), os.path.expanduser("~/.local"),
    os.path.expanduser("~/.firefox"), os.path.expanduser("~/.mozilla"),
    os.path.expanduser("~/.gnupg"), os.path.expanduser("~/.ssh"),
    os.path.expanduser("~/.npm"), os.path.expanduser("~/.yarn"),
    os.path.expanduser("~/.python"), os.path.expanduser("~/.thunderbird")
]

def dirs():
    global _KEY_ID, KEY_DIR
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR, exist_ok=True)

    if not os.path.exists(KEY_PATH):
        os.makedirs(KEY_PATH, exist_ok=True)

    if not os.path.exists(KEY_DIR):
        _KEY_ID = generateID()
        KEY_DIR = os.path.join(KEY_PATH, f"{_KEY_ID}.key")

def generateID():
    return uuid.uuid4().int
