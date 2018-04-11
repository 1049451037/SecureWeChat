import rsa
import requests

class GetKey(object): # 仅仅做调试用，服务器端使用了简单的文件下载服务
    def __init__(self):
        pass
    def public_key(self, username):
        return rsa.PublicKey.load_pkcs1(requests.get('http://172.22.109.231:8001/'+username+'_pub.pem').content)
    def private_key(self, username): # 这个函数本来不应该存在，为调试方便才有的
        return rsa.PrivateKey.load_pkcs1(requests.get('http://172.22.109.231:8001/'+username+'_pri.pem').content)