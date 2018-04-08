import itchat
from itchat.content import TEXT
import rsa

s = []

@itchat.msg_register(TEXT, isFriendChat=True)
def store_msg(msg):
    if not msg['FromUserName']==myUserName:
        s.append(msg)
    return None # 'I received: ' + msg.text

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg['NickName']=='微信测试群' and msg.isAt:
        msg.user.send(u'@%s\u2005I received: %s' % (msg.actualNickName, msg.text))
    elif msg['NickName']=='微信测试群':
        itchat.send(u'I received: %s'(msg.text), iRoom['UserName'])

itchat.auto_login(True)
myUserName = itchat.get_friends(update=True)[0]["UserName"]
itchat.run(blockThread=False)
iRoom = itchat.search_chatrooms('微信测试群')[0]
# iRoom.send(u'测试消息2')
# itchat.send(u'测试消息', iRoom['UserName'])
(bob_pub, bob_priv) = rsa.newkeys(512)
while True:
    order = input('等待命令输入，请输入数字 1. 显示当前消息；2. 发送消息；其他. 退出程序：')
    if order=='1':
        print(len(s), '条消息')
        for msg in s:
            print(type(msg['Content']))
            news = msg['Content'].encode('ascii')
            print(news[0])
            print(news[1])
            print(news[2])
            print(type(news))
            crypto = []
            for i in range(0, len(news), 8):
                num = 0
                for j in range(8):
                    num = (num<<1) | (news[i+7-j]-ord('0'))
                crypto.append(num)
            crypto = bytes(crypto)
            print(crypto)
            message = rsa.decrypt(crypto, bob_priv)
            print(message.decode('utf8'))
    elif order=='2':
        message = 'hello Bob!'.encode('utf8')
        crypto = rsa.encrypt(message, bob_pub)
        print(crypto)
        name = input('请输入要发送的对象昵称或备注：')
        author = itchat.search_friends(name=name)
        if len(author)>0:
            #text = input('请输入消息内容：')
            #author[0].send(text)
            L = len(crypto)
            mynews = b''
            for i in range(L):
                for j in range(8):
                    thbit = (crypto[i]>>j)&1
                    thchar = chr(ord('0')+thbit)
                    mynews += thchar.encode('ascii')
            author[0].send(mynews.decode('ascii'))
        else:
            print('未找到该用户！')
    else:
        break
itchat.logout()

