import RSAClass
import sys

cipher = RSAClass.RSAClass()  # creating the cipher


def store_credentials (username, password, host):
    credentials = [username, password]  # creating a list to pass to the cipher to encrypt
    cipher.encrypt_and_store(credentials, host)  # encrypting and storing the credentials for host


def get_credentials (host):
    return cipher.retrieve_and_decrypt(host)  # retrieving and decrypting the credentials for host

    
def removeEntry():
    print("remove")


#store_credentials('usernaffamasasae', 'pad', 'utdad.edu')
#print(get_credentials('utdad.edu'))