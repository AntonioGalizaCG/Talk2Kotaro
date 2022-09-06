#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

current_dir = os.getcwd()

def encrypt(filename,key):
    file_to_encrypt = filename
    buffer_size = 65536 # 64kb
    # === Encrypt ===
    # Open the input and output files
    input_file = open(file_to_encrypt, 'rb')
    output_file = open(file_to_encrypt + '.encrypted', 'wb')
    # Create the cipher object and encrypt the data
    cipher_encrypt = AES.new(key, AES.MODE_CFB)
    # Initially write the iv to the output file
    output_file.write(cipher_encrypt.iv)
    # Keep reading the file into the buffer, encrypting then writing to the new file
    buffer = input_file.read(buffer_size)
    while len(buffer) > 0:
        ciphered_bytes = cipher_encrypt.encrypt(buffer)
        output_file.write(ciphered_bytes)
        buffer = input_file.read(buffer_size)
    # Close the input and output files
    input_file.close()
    output_file.close()

# === Decrypt ===
def decrypt(filename,key):
# Open the input and output files
    file_to_encrypt = filename
    print(1)
    buffer_size = 65536 # 64kb
    input_file = open(file_to_encrypt, 'rb')
    print(2)
    output_file = open(file_to_encrypt + '.decrypted', 'wb')
    print(3)
    # Read in the iv
    iv = input_file.read(16)
    print(4)
    # Create the cipher object and encrypt the data
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
# # === Proving the data matches (hash the files and compare the hashes) ===
# import hashlib
#
# def get_file_hash(file_path):
#     block_size = 65536
#     file_hash = hashlib.sha256()
#     with open(file_path, 'rb') as f:
#         fb = f.read(block_size)
#         while len(fb) > 0:
#             file_hash.update(fb)
#             fb = f.read(block_size)
#     return file_hash.hexdigest()
#
# assert get_file_hash(file_to_encrypt) == get_file_hash(file_to_encrypt + '.decrypted'), 'Files are not identical'
