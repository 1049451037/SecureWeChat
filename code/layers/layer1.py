import itchat
from itchat.content import TEXT
import rsa

GroupName = '微信测试群'
msgs = []

@itchat.msg_register(TEXT, isGroupChat=True)
def receive_msg(msg):
    #if msg['NickName']==GroupName: # 这里好像还有一个bug
    msgs.append(msg.text)
    #print(msgs)

class Broadcasting(object):
    def __init__(self, groupname):
        itchat.auto_login(True)
        GroupName = groupname
        itchat.run(blockThread=False)
        self.room = itchat.search_chatrooms(GroupName)[0]
        self.room = itchat.update_chatroom(self.room['UserName'], detailedMember=True)
    def send(self, text):
        self.room.send(text)
    def receive(self):
        return msgs