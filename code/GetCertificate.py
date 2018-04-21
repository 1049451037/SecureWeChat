from services.keys import GetKey
from ca.layer2 import ByteStreamCA as bsca
import rsa
import pickle
import time

mylayer = bsca('smallcoder')
gk = GetKey()
name = input('请输入姓名：')
sex = input('请输入性别：')
mail = input('请输入邮箱：')
dic = {'name': name, 'sex': sex, 'mail': mail, 'key': gk.get_self_pubkey()}
message = pickle.dumps(dic)
mylayer.send(message)
print('正在等待回复……')
time.sleep(5)
signature = mylayer.receive()[0]
pubkey = rsa.PublicKey.load_pkcs1(gk.get_ca_pubkey())
print(rsa.verify(message, signature, pubkey))
with open('cert/cert.pkl', 'wb') as f:
    f.write(message)
with open('cert/cert_sig', 'wb') as f:
    f.write(signature)