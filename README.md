# Cipher Encryptor 🔐

**Cipher Encryptor** is a simple command-line file and directory encryption/decryption tool written in Python using PyNaCl (libsodium).  
It allows you to securely encrypt files with a secret key, while providing safety checks for sensitive directories.
**Linux Only**
---

## Features

- Encrypt and decrypt individual files or entire directories.
- Automatically detects and warns about **sensitive directories** (e.g., `/`, `~/.config`, `~/.ssh`).
- Prints a **tree view** of the files to be encrypted for clarity.
- Double confirmation before performing destructive operations.
- Uses **PyNaCl** for strong symmetric encryption (libsodium backend).
- Stores encryption keys securely in the user config directory.

---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/cipher-encryptor.git
cd cipher-encryptor
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
Requirements:
  Python 3+
  [PyNaCl](https://pypi.org/project/PyNaCl)
  [Questionary](https://pypi.org/project/questionary/)

---

## Usage:

Run the main script:
```bash
chmod +x ./cipher.py
```
```bash
python cipher.py
```
Choose Encrypt or Decrypt.

Select a file or directory from the current working directory.

If the directory is sensitive, confirm the operation.

The program will recursively encrypt/decrypt files using a secure secret key.

---

## Sensitive Directories

Cipher Encryptor warns before modifying critical directories, including but not limited to:

`~/.config`

`~/.cache`

`~/.local`

`~/.ssh`

`~/.gnupg`

`~/.mozilla` / `~/.firefox`

`~/.npm` / `~/.yarn`

`~/.python`

`~/.thunderbird`

I have not added `/*` dirs because you'll need root `sudo`

Always confirm before encrypting/decrypting these folders.

---

## Security Notes

The secret key is stored under ~/.config/cipher/key/.

Files are permanently overwritten after encryption/decryption.

Use with caution; the author is not responsible for data loss.

---

## Acknowledgements

- PyNaCl
   for cryptography backend
- Questionary
   for interactive CLI menus

---
