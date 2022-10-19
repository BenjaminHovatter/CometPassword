import hashlib


class Sha:
    def encrypt(self, str):
        hashtag = hashlib.sha256(str.encode('utf-8')).hexdigest()
        return hashtag


s = Sha
print(s.encrypt(s,  "asdaasdfafssda"))
