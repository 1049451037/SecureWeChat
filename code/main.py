from ca.layer2 import ByteStreamCA as bsca
from layers.layer3 import P2P as pp
from layers.services.keys import GetKey
import rsa
import pickle
import time

def GetCertificate(name):
    mylayer = bsca(name)
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
    ca_pubkey = rsa.PublicKey.load_pkcs1(gk.get_ca_pubkey())
    if rsa.verify(message, signature, ca_pubkey):
        print('认证成功！')
        with open('cert/cert.pkl', 'wb') as f:
            f.write(message)
        with open('cert/cert_sig', 'wb') as f:
            f.write(signature)
        trust = {gk.get_self_pubkey(): dic}
        with open('trust.pkl', 'wb') as f:
            pickle.dump(trust, f)
    mylayer.logout()

if __name__ == '__main__':
    CA = 'smallcoder'
    gk = GetKey()
    try:
        with open('cert/cert.pkl', 'rb') as f:
            cert = f.read()
        with open('cert/cert_sig', 'rb') as f:
            cert_sig = f.read()
        ca_pubkey = rsa.PublicKey.load_pkcs1(gk.get_ca_pubkey())
        if not rsa.verify(cert, cert_sig, ca_pubkey):
            GetCertificate(CA)
    except:
        GetCertificate(CA)
    mylayer = pp('微信测试群')
    while True:
        o = input('1. 接收消息；2. 发送消息；3. 显示好友列表；4. 广播自己的公钥；其他. 退出程序\n等待命令输入，请输入数字：')
        if o=='1':
            msgs = mylayer.receive()
            print('共有' + str(len(msgs)) + '条消息')
            for msg in msgs:
                print(msg)
        elif o=='2':
            text = input('请输入消息内容：')
            friends = list(mylayer.trust.items())
            for i in range(len(friends)):
                print(i, friends[i][1]['name'], friends[i][1]['sex'], friends[i][1]['mail'])
            id = int(input('请输入对方编号：'))
            mylayer.send(text.encode('utf8'), friends[i][0])
        elif o=='3':
            friends = list(mylayer.trust.items())
            for i in range(len(friends)):
                print(i, friends[i][1]['name'], friends[i][1]['sex'], friends[i][1]['mail'])
        elif o=='4':
            mylayer.send('hello'.encode('utf8'), gk.get_self_pubkey())
        else:
            break
    mylayer.logout()