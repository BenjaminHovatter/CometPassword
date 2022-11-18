import rsa
import os


class RSAClass:

    def __init__(self):
        self.private_key = -1
        self.public_key = -1

    def encrypt(self, credentials):
        entry = credentials[0] + ',' + credentials[1]  # csv-> username and password
        encrypted_credentials = rsa.encrypt(entry.encode(), self.public_key)  # encrypting using RSA public key
        return encrypted_credentials

    def encrypt_and_store(self, credentials, host):
        if (self.private_key == -1) or (self.public_key == -1):
            self.init_keys()

        encrypted_credentials = self.encrypt(credentials)
        f = open('./Hosts/' + host, 'wb')
        f.write(encrypted_credentials)

    def retrieve_and_decrypt(self, host):
        if (self.private_key == -1) or (self.public_key == -1):
            self.init_keys()
        d = {}

        f = open('./Hosts/' + host, 'rb')  # opening file that contains the credentials of the user on this host/service.
        encrypted = f.read()  # reading the encrypted bytes
        decrypted_credentials = rsa.decrypt(encrypted, self.private_key).decode()  # decrypting using RSA private key
        (username, password) = decrypted_credentials.split(',')  # separating the username and password
        d[username] = password

        return d

    def init_keys(self):
        # generating or retrieving already-generated keys

        f = open('./Keys', 'a')  # creates empty file if it does not exist
        file_size = os.path.getsize('./Keys')  # retrieve size of the file

        if file_size == 0:  # first time user creates RSA credentials
            self.public_key, self.private_key = rsa.newkeys(512)
            f.write(str(self.private_key['n']) + '\n')
            f.write(str(self.private_key['e']) + '\n')
            f.write(str(self.private_key['d']) + '\n')
            f.write(str(self.private_key['p']) + '\n')
            f.write(str(self.private_key['q']))

        else:  # user already has RSA credentials
            with open('./Keys') as f:
                lines = f.read().splitlines()

            # retrieving RSA parameters
            n = int(lines[0])
            e = int(lines[1])
            d = int(lines[2])
            p = int(lines[3])
            q = int(lines[4])
            self.public_key = rsa.PublicKey(n, e)
            self.private_key = rsa.PrivateKey(n, e, d, p, q)
