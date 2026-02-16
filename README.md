# Cipher Encryptor 🔐

**Cipher Encryptor** is a simple command-line file and directory encryption/decryption tool written in Python using PyNaCl (libsodium).  
It allows you to securely encrypt files with a secret key, while providing safety checks for sensitive directories.

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
---

2. Install dependencies:

```bash
pip install -r requirements.txt
```

**Requirements**:
- Python3+
- [PyNaCl](https://pypi.org/project/questionary/)
- [Questionary](https://pypi.org/project/PyNaCl/)

---

## Usage:

Run the main script:
```bash
python cipher.py
```
1. Choose Encrypt or Decrypt.

2. Select a file or directory from the current working directory.

3. If the directory is sensitive, confirm the operation.

4. The program will recursively encrypt/decrypt files using a secure secret key.

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

Always confirm before encrypting/decrypting these folders.
I have not added `/` directories because you will need root.

---

## Security Notes

The secret key is stored under `~/.config/cipher/key/`.

Files are permanently overwritten after encryption/decryption.

Use with caution; the author is not responsible for data loss.

---

## License

This project is licensed under the GPL v3 License. See LICENSE
 for details.

---

## Acknowledgements

PyNaCl
 for cryptography backend
Questionary
 for interactive CLI menus

---

## TODO:

 - Key selector to encript with different keys
 - Key remover
 - Key creator
