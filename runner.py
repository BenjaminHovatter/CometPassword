import RSA

cipher = RSA.RSA()  # creating the cipher

username = 'username'
password = 'password'

credentials = [username, password]  # creating a list to pass to the cipher to encrypt

cipher.encrypt_and_store(credentials, 'utdallas.edu')  # encrypting and storing the credentials for host
print(cipher.retrieve_and_decrypt('utdallas.edu'))  # retrieving and decrypting the credentials for host
