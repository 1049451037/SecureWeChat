import itchat
from itchat.content import TEXT

s = []

@itchat.msg_register(TEXT, isFriendChat=True, isGroupChat=True, isMpChat=True)
def store_msg(msg):
    if not msg['FromUserName']==myUserName:
        s.append(msg)
    return 'I received: ' + msg.text

itchat.auto_login(True)
myUserName = itchat.get_friends(update=True)[0]["UserName"]
itchat.run(blockThread=False)
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

