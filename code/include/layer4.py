'''
APP层
收发消息的功能事实上是基于layer3的APP，应该整理到这里，而不是放在main里面
而且这样也可以扩展出很多其他APP
'''

from .layer3 import P2P
from .services.keys import GetKey
import rsa

class Chat(object):
    def __init__(self, groupname):
        self.down = P2P(groupname)
    def send(self):
        friends = list(self.down.trust.items())
        for i in range(len(friends)):
            print(i, friends[i][1]['name'], friends[i][1]['sex'], friends[i][1]['mail'])
        id = int(input('请输入你要发送的对象的编号，输入不在范围内的编号视作放弃发送：'))
        if id>=len(friends) or id<0:
            return
        text = input('请输入消息内容：')
        self.down.send(text.encode('utf8'), friends[id][0])
    def receive(self):
        msgs = self.down.receive()
        print('共有' + str(len(msgs)) + '条消息')
        for msg in msgs:
            print(msg)
    def show_friends(self):
        friends = list(self.down.trust.items())
        for i in range(len(friends)):
            print(i, friends[i][1]['name'], friends[i][1]['sex'], friends[i][1]['mail'])
    def broadcast(self):
        gk = GetKey()
        self.down.send('hello'.encode('utf8'), gk.get_self_pubkey())
    def logout(self):
        self.down.logout()