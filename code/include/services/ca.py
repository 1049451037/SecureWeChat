from .calayers.calayer2 import ByteStreamCA as bsca
from .keys import GetKey
import time
import pickle
import rsa

def GetCertificate(name):
    gk = GetKey()
    try:
        with open('cert/cert.pkl', 'rb') as f:
            cert = f.read()
        with open('cert/cert_sig', 'rb') as f:
            cert_sig = f.read()
        ca_pubkey = rsa.PublicKey.load_pkcs1(gk.get_ca_pubkey())
        if rsa.verify(cert, cert_sig, ca_pubkey):
            return
    except:
        pass
    print('这是你第一次来到这里，你将要做的是一件非常神圣的事情，那就是公钥认证')
    print('目前唯一的公钥认证是一个叫做smallcoder的公众号，所以在认证之前要先关注这个公众号')
    input('请保证你输入的是准确的，以保证你与好友的安全交流，按回车继续……')
    mylayer = bsca(name)
    print('现在开始认证——')
    name = input('请输入姓名：')
    sex = input('请输入性别：')
    mail = input('请输入邮箱：')
    dic = {'name': name, 'sex': sex, 'mail': mail, 'key': gk.get_self_pubkey()}
    message = pickle.dumps(dic)
    mylayer.send(message)
    print('正在等待回复……')
    time.sleep(10)
    signature = mylayer.receive()[0]
    ca_pubkey = rsa.PublicKey.load_pkcs1(gk.get_ca_pubkey())
    if rsa.verify(message, signature, ca_pubkey):
        with open('cert/cert.pkl', 'wb') as f:
            f.write(message)
        with open('cert/cert_sig', 'wb') as f:
            f.write(signature)
        trust = {gk.get_self_pubkey(): dic}
        with open('trust.pkl', 'wb') as f:
            pickle.dump(trust, f)
        print('恭喜你认证成功！之所以认证如此顺利，是因为目前认证机构仍处于调试阶段，所以并不会对你输入的信息真实性做核查')
        input('现在仍然要提醒一下，请保护好你本地的cert文件夹，这个文件夹是你在这里身份的标识，不要上传到网络，按回车继续……')
    mylayer.logout()
    input('初始的时候你的好友列表里只有你自己，如果想跟他人聊天，可以通过广播自己的公钥来让别人知道你的存在，按回车继续……')
