import itchat
from itchat.content import TEXT

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
while True:
    ord = input('等待命令输入，请输入数字 1. 显示当前消息；2. 发送消息；其他. 退出程序：')
    if ord=='1':
        print(len(s), '条消息')
        for msg in s:
            print(msg['User']['NickName'] + ': ' + msg['Content'])
    elif ord=='2':
        name = input('请输入要发送的对象昵称或备注：')
        author = itchat.search_friends(name=name)
        if len(author)>0:
            text = input('请输入消息内容：')
            author[0].send(text)
        else:
            print('未找到该用户！')
    else:
        break
itchat.logout()

