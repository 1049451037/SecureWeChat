import rsa
import requests

class GetKey(object): # 仅仅做调试用，服务器端使用了https://github.com/hanxi/http-file-server提供简单的文件下载服务，把generate_pubkey.py生成的公钥私钥拷贝进去，但是username会变……很尴尬，唯一标识的问题还没有解决
    def __init__(self):
        self.ip = ''
    def public_key(self, username):
        return rsa.PublicKey.load_pkcs1(requests.get('http://'+ip+'/'+username+'_pub.pem').content)
    def private_key(self, username): # 这个函数本来不应该存在，为调试方便才有的
        return rsa.PrivateKey.load_pkcs1(requests.get('http://'+ip+'/'+username+'_pri.pem').content)