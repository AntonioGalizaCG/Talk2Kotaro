#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

## @package encryption
## Contains all functions related to AES encryption for the Talk to Kotaro web
## platform.

## current directory where the script is being executed.
current_dir = os.getcwd()


## encrypts a file using AES256.
## @param filename name of the file to be encrypted.
## @param key private key to be used to encrypt the file.
def encrypt(filename, key):
    ## file to be encrypted from the filename; str.
    file_to_encrypt = filename
    ## buffer size in bytes for the encryption process; int.
    buffer_size = 65536 # 64kb
    # === Encrypt ===
    ## file to be encrypted; file.
    input_file = open(file_to_encrypt, 'rb')
    ## encrypted file; file.
    output_file = open(file_to_encrypt + '.encrypted', 'wb')
    ## cipher object and encrypted data
    cipher_encrypt = AES.new(key, AES.MODE_CFB)
    # Initially write the iv to the output file
    output_file.write(cipher_encrypt.iv)
    # Keep reading the file into the buffer, encrypting then writing to the new file
    buffer = input_file.read(buffer_size)
    while len(buffer) > 0:
        ## ciphered bytes of the input file.
        ciphered_bytes = cipher_encrypt.encrypt(buffer)
        output_file.write(ciphered_bytes)
        buffer = input_file.read(buffer_size)
    # Close the input and output files
    input_file.close()
    output_file.close()


## decrypts the file
def decrypt(filename,key):
    ## file to be decrypted from the filename; str.
    file_to_encrypt = filename
    print(1)
    ## buffer size in bytes for the decryption process; int.
    buffer_size = 65536 # 64kb
    ## Opened file for decryption; file.
    input_file = open(file_to_encrypt, 'rb')
    print(2)
    ## Decrypted file.
    output_file = open(file_to_encrypt + '.decrypted', 'wb')
    print(3)
    ## Read in the iv
    iv = input_file.read(16)
    print(4)
    ## cipher object and encrypted data
    cipher_encrypt = AES.new(key, AES.MODE_CFB, iv=iv)
    print(5)
    # Keep reading the file into the buffer, decrypting then writing to the new file
    buffer = input_file.read(buffer_size)
    print(6)
    while len(buffer) > 0:
        decrypted_bytes = cipher_encrypt.decrypt(buffer)
        output_file.write(decrypted_bytes)
        buffer = input_file.read(buffer_size)
    print(7)
    # Close the input and output files
    input_file.close()
    output_file.close()
    print("finished")
