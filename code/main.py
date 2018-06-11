from include.layer4 import Chat
from include.services.ca import GetCertificate

if __name__ == '__main__':
    CA = 'runningANDdancing'
    GetCertificate(CA)
    chatroom = '微信测试群'
    chat = Chat(chatroom)
    while True:
        o = input('1. 接收消息；2. 发送消息；3. 显示好友列表；4. 广播自己的公钥；其他. 退出程序\n等待命令输入，请输入数字：')
        if o=='1':
            chat.receive()
        elif o=='2':
            chat.send()
        elif o=='3':
            chat.show_friends()
        elif o=='4':
            chat.broadcast()
        else:
            break
    chat.logout()