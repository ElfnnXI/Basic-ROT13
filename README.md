# ⚡ Basic ROT13 Cipher

ROT13 is a simple implementation of the **ROT13 cipher**, an example of the classic cryptographic technique of substitution ciphers used in data security. ROT13 stands for "rotate by 13 places", and works by shifting each letter of the alphabet 13 positions forward. Since there are 26 letters in the alphabet, ROT13 applies two rotations to restore the original text.

#### ⚒️ How It Works
Each letter in the input string is replaced by the letter 13 positions later in the alphabet. If the shift goes past the end of the alphabet, it will return to the beginning. ROT13 only operates on alphabetic characters (A-Z and a-z), so numbers, symbols, and spaces are not changed.

## 🪶 Features

* Applying ROT13 twice will restore the original input.
* Only the alphabetic characters are encoded, everything else is unchanged.
* A lightweight process with no dependencies required, easy to understand and implement.
 * Excellent for learning basic decryption encryption concepts.


## ⭐ Requirements

* Python 3.x

## 👇 How to Use

1. Clone this repository:

```bash
git clone https://github.com/ElfnnXI/Basic-ROT13.git
cd Basic-ROT13
```

2. Run the script:

```bash
python start.py
```

3. Choose to encrypt or decrypt a message and enter your text.

## Example
##### Encryption:
```
=== ROT13 Cipher ===
Choose an option:
1. Encrypt a message
2. Decrypt a message
Enter your choice (1/2): 1
Enter the message: You are so beautiful
Result: Lbh ner fb ornhgvshy

```
##### Decryption:
```
=== ROT13 Cipher ===
Choose an option:
1. Encrypt a message
2. Decrypt a message
Enter your choice (1/2): 2
Enter the message: Lbh ner fb ornhgvshy
Result: You are so beautiful
```

---
## 🧑‍💻 Author
Ikmal Thaufan Mahdi
GitHub: @ElfnnXI

