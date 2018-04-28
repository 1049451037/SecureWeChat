'''
P2P层，实现点对点安全通信的字节流信道

About send()
使用pickle字典作为P2P层的消息传输方法，消息字段有：
    cert: digital certificate
    cert_sig: signature of CA
    symkey: symmetric key encrypted by target_pubkey
    message: message data encrypted by symkey
    sig: signature of message

About receive()
receive要做的事情有三个：
1. 收到消息以后会自动认证一下，把认证成功的公钥加入好友名单。
2. 公钥认证好以后，解密消息，确认数字签名。
3. 确认好以后，把消息加入队列。

trust.pkl用来保存已经认证公钥的好友，数据结构是一个字典，由pubkey映射到用户信息
'''

from .layer2 import ByteStreamBroadcast as bsbc
import rsa
import pickle
from cryptography.fernet import Fernet
from .services.keys import GetKey
import random
import json

class P2P(object):
    def __init__(self, groupname):
        self.down = bsbc(groupname)
        self.gk = GetKey()
        with open('trust.pkl', 'rb') as f:
            self.trust = pickle.load(f)
        with open('cert/cert.pkl', 'rb') as f:
            self.cert = f.read()
        with open('cert/cert_sig', 'rb') as f:
            self.cert_sig = f.read()
        self.init_counter()

    def init_counter(self):
        '''
        init send counter at initialization
        '''
        js_list = None
        try:
            with open('contact/contact_list.json', 'r') as fin:
                self.js_list = json.load(fin)
        except FileNotFoundError:
            pass
        if js_list == None:
            self.current_n = random.randint(1, 100000)
            self.next_n = random.randint(1, 100000)
            self.receive_dict = {}
            self.js_list = {
                'current_n': self.current_n,
                'next_n': self.next_n,
                'receive_dict': self.receive_dict
                 }
        else:
            self.current_n = self.js_list['current_n']
            self.next_n = self.js_list['next_n']
            self.receive_dict = self.js_list['receive_dict']

    def update_in_receive(self, name, next_n):
        '''
        update receive_dict in receiving message
        '''
        self.receive_dict[name] = next_n
        self.js_list['receive_dict'] = self.receive_dict
        with open('contact/contact_list.json', 'w') as fou:
            json.dump(self.js_list, fou)

    def update_in_send(self):
        '''
        update current_n and next_n in sending message
        '''
        print('update in send!')
        print(self.current_n)
        print(self.next_n)
        self.current_n = self.next_n
        self.next_n = random.randint(1, 100000)
        self.js_list['current_n'] = self.current_n
        self.js_list['next_n'] = self.next_n
        with open('contact/contact_list.json', 'w') as fou:
            json.dump(self.js_list, fou)

    def send(self, message, target_pubkey, broadcast=False): # message is bytestream
        self_prikey = rsa.PrivateKey.load_pkcs1(self.gk.get_self_prikey())
        target_pubkey = rsa.PublicKey.load_pkcs1(target_pubkey)
        dic = {'cert': self.cert, 'cert_sig': self.cert_sig}
        symkey = Fernet.generate_key()
        f = Fernet(symkey)
        sig = rsa.sign(message, self_prikey, 'SHA-256')
        dic['sig'] = sig
        message = f.encrypt(message)
        dic['message'] = message
        symkey = rsa.encrypt(symkey, target_pubkey)
        dic['symkey'] = symkey
        if broadcast == False:
            dic['current_n'] = str(self.current_n).encode('utf-8')
            dic['next_n'] = str(self.next_n).encode('utf-8')
            self.update_in_send()
        self.down.send(pickle.dumps(dic))

    def receive(self):
        self_prikey = rsa.PrivateKey.load_pkcs1(self.gk.get_self_prikey())
        msgs = []
        for msg in self.down.receive():
            try:
                dic = pickle.loads(msg)
                cert = dic['cert']
                cert_sig = dic['cert_sig']
                ca_pubkey = rsa.PublicKey.load_pkcs1(self.gk.get_ca_pubkey())
                info = pickle.loads(cert)
                if rsa.verify(cert, cert_sig, ca_pubkey):
                    self.trust[info['key']] = info
                    symkey = rsa.decrypt(dic['symkey'], self_prikey)
                    f = Fernet(symkey)
                    message = f.decrypt(dic['message'])
                    try:
                        current_n = dic['current_n'].decode('utf-8')
                        next_n = dic['next_n'].decode('utf-8')
                    except KeyError:
                        pass
                    pubkey = rsa.PublicKey.load_pkcs1(info['key'])
                    if rsa.verify(message, dic['sig'], pubkey):
                        if info['name'] not in self.receive_dict:
                            self.update_in_receive(info['name'], next_n)
                            msgs.append((message.decode('utf-8'), info['name'], info['sex'], info['mail']))
                        elif self.receive_dict[info['name']] == current_n:
                            self.update_in_receive(info['name'], next_n)
                            msgs.append((message.decode('utf-8'), info['name'], info['sex'], info['mail']))

            except Exception as e:
                print(e)
        return msgs
    def logout(self):
        with open('trust.pkl', 'wb') as f:
            pickle.dump(self.trust, f)
        self.down.logout()