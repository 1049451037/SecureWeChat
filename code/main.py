from layers.layer3 import P2P as pp
from services.keys import GetKey
import rsa

mylayer = pp('微信测试群')
gk = GetKey()
while True:
    ord = input('等待命令输入，请输入数字 1. 接收消息；2. 发送消息；3. 显示成员列表；其他. 退出程序：')
    if ord=='1':
        for username in mylayer.showmembers():
            print(username, mylayer.receive(gk.private_key(username)))
    elif ord=='2':
        text = input('请输入消息内容：')
        members = mylayer.showmembers()
        for i in range(len(members)):
            print(str(i) + '.', members[i])
        id = int(input('请选择对方username编号'))
        mylayer.send(text, gk.public_key(members[id]))
    elif ord=='3':
        print(mylayer.showmembers())
    else:
        break
mylayer.logout()