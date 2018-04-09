import itchat
from itchat.content import TEXT

GroupName = '微信测试群'
msgs = []

@itchat.msg_register(TEXT, isGroupChat=True)
def receive_msg(msg):
    msgs.append(msg.text) # 自己发的消息是否也会进来？如何判断仅属于GroupName的消息才接收？

class CharStreamBroadcast(object):
    def __init__(self, groupname):
        itchat.auto_login(True)
        GroupName = groupname
        itchat.run(blockThread=False)
        self.room = itchat.search_chatrooms(GroupName)[0]
        self.room = itchat.update_chatroom(self.room['UserName'], detailedMember=True)
    def send(self, charstream):
        self.room.send(charstream)
    def receive(self):
        return msgs