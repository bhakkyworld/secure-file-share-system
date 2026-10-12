README.md
# Secure File Sharing System

## Problem Statement
Sharing sensitive files over insecure networks exposes data to interception and unauthorized access. This project provides a robust system to encrypt and decrypt files securely using AES encryption.

## Objectives
- Implement AES-256 GCM encryption for file confidentiality.
- Provide a user-friendly interface using Streamlit.
- Support file encryption and key management.

## Technologies Used
- Python 3.x
- Streamlit
- Cryptography Library

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run app: `streamlit run app.py`

https://github.com/bhakkyworld/secure-file-share-system/blob/main/app.py
Project Demonstration

Workflow Overview:
1.Sender Side (Encryption):
Open the Encrypt File tab.
Upload any document or image.
Click Generate Key & Encrypt.
Download both the encrypted file (filename.enc) and the secret key (secret.key).
Send the .enc file to the recipient via any channel, and share the .key via a secure channel.
2.Receiver Side (Decryption):
Open the Decrypt File tab.
Upload the received .enc file and the corresponding .key file.
Click Decrypt File.
Download the restored original file.

 
 Cryptography & Network Security Concepts Used

Symmetric Key Cryptography (AES-256): Uses the Advanced Encryption Standard (AES) with a 256-bit key for fast and high-security encryption/decryption.

Authenticated Encryption with Associated Data (AEAD - AES-GCM): Combines Galois/Counter Mode with AES to provide both confidentiality and built-in message integrity checking.

Cryptographic Nonce: Uses a unique 12-byte initialization vector (nonce) for every encryption process to prevent replay and pattern attacks.

Data Integrity Verification: Automatically detects if an encrypted file or secret key has been tampered with or corrupted during decryption
