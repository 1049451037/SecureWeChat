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

mylayer = pp('微信测试群')
while True:
    ord = input('等待命令输入，请输入数字 1. 接收消息；2. 发送消息；3. 显示成员列表；其他. 退出程序：')
    if ord=='1':
        print(mylayer.receive())
    elif ord=='2':
        to = input('请输入对方昵称：')
        text = input('请输入消息内容：')
        mylayer.send(to, text)
    elif ord=='3':
        print(mylayer.showmembers())
    else:
        break