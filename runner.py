import RSAClass
import sys

cipher = RSAClass.RSAClass()  # creating the cipher


def store_credentials (username, password, host):
    credentials = [username, password]  # creating a list to pass to the cipher to encrypt
    cipher.encrypt_and_store(credentials, 'utdallas.edu')  # encrypting and storing the credentials for host


def get_credentials (host):
    return cipher.retrieve_and_decrypt('utdallas.edu')  # retrieving and decrypting the credentials for host


store_credentials('username', 'password', 'utdallas.edu')
print(get_credentials('utdallas.edu'))