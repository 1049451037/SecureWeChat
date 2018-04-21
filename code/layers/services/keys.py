import requests
import os
import rsa

class GetKey(object):
    def __init__(self):
        pass
    def get_self_pubkey(self):
        try:
            with open('cert/pub.pem', 'rb') as f:
                return f.read()
        except:
            os.makedirs('cert', exist_ok=True)
            (pubkey, prikey) = rsa.newkeys(512)
            with open('cert/pub.pem', 'wb') as f:
                f.write(pubkey.save_pkcs1())
            with open('cert/pri.pem', 'wb') as f:
                f.write(prikey.save_pkcs1())
            with open('cert/pub.pem', 'rb') as f:
                return f.read()
    def get_self_prikey(self):
        try:
            with open('cert/pri.pem', 'rb') as f:
                return f.read()
        except:
            os.makedirs('cert', exist_ok=True)
            (pubkey, prikey) = rsa.newkeys(512)
            with open('cert/pub.pem', 'wb') as f:
                f.write(pubkey.save_pkcs1())
            with open('cert/pri.pem', 'wb') as f:
                f.write(prikey.save_pkcs1())
            with open('cert/pub.pem', 'rb') as f:
                return f.read()
    def get_ca_pubkey(self):
        try:
            with open('cert/capub.pem', 'rb') as f:
                return f.read()
        except:
            pubkey = requests.get('http://1049451037.github.io/file/cakey/pub.pem').content
            os.makedirs('cert', exist_ok=True)
            with open('cert/capub.pem', 'wb') as f:
                f.write(pubkey)
            return pubkey