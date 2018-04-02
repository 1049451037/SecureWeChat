import itchat
from itchat.content import TEXT

GroupName = '微信测试群'
msgs = []

@itchat.msg_register(TEXT, isGroupChat=True)
def receive_msg(msg):
    if msg['NickName']==GroupName: # 这里好像还有一个bug
        msgs.append(msg)
    #if msg['NickName']==GroupName and msg.isAt:
    #    msg.user.send(u'@%s\u2005I received: %s' % (msg.actualNickName, msg.text))
    #elif msg['NickName']==GroupName:
    #    itchat.send(u'I received: %s'(msg.text), iRoom['UserName'])

class Broadcasting(object):
    def __init__(self, groupname):
        itchat.auto_login(True)
        itchat.run(blockThread=False)
        GroupName = groupname
        self.room = itchat.search_chatrooms('微信测试群')[0]
        self.room = itchat.update_chatroom(self.room['UserName'], detailedMember=True)
    def send(self, text):
        self.room.send(text)
    def receive(self):
        return msgs