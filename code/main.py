'''
from layers.layer1 import Broadcasting as bc

mylayer = bc('微信测试群')
while True:
    ord = input('等待命令输入，请输入数字 1. 接收消息；2. 发送消息；其他. 退出程序：')
    if ord=='1':
        print(mylayer.receive())
    elif ord=='2':
        text = input('请输入消息内容：')
        mylayer.send(text)
    else:
        break
'''
from layers.layer2 import P2P as pp
import rsa

mylayer = pp('微信测试群')
(pubkey, prikey) = rsa.newkeys(512)
while True:
    ord = input('等待命令输入，请输入数字 1. 接收消息；2. 发送消息；3. 显示成员列表；其他. 退出程序：')
    if ord=='1':
        print(mylayer.receive(prikey))
    elif ord=='2':
        text = input('请输入消息内容：')
        mylayer.send(text, pubkey)
    elif ord=='3':
        print(mylayer.showmembers())
    else:
        break