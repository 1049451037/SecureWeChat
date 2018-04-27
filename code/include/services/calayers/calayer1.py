import itchat
from itchat.content import TEXT

CAName = 'smallcoder'
msgs = []

@itchat.msg_register(TEXT, isMpChat=True)
def receive_msg(msg):
    if msg['User']['NickName']==CAName:
        msgs.append(msg.text)

class CharStreamCA(object):
    def __init__(self, caname):
        itchat.auto_login(True)
        CAName = caname
        itchat.run(blockThread=False)
        mps = itchat.get_mps()
        mps = itchat.search_mps(name=CAName)
        for i in range(len(mps)):
            print(str(i) +'.', mps[i]['NickName'])
        id = int(input('找到' + str(len(mps)) + '个公钥认证机构，请输入你想要去认证的机构编号：'))
        self.ca = mps[id]
        # myInfo = itchat.get_friends(update=True)[0]
        # print(myInfo)
    def send(self, charstream):
        self.ca.send(charstream)
    def receive(self):
        return msgs
    def logout(self):
        itchat.logout()