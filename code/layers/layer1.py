import itchat
from itchat.content import TEXT

# https://www.python.org/dev/peps/pep-0318/
# https://stackoverflow.com/questions/6392739/what-does-the-at-symbol-do-in-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143186781871161bc8d6497004764b398401a401d4cce000

GroupName = '微信测试群'
msgs = []

@itchat.msg_register(TEXT, isGroupChat=True)
def receive_msg(msg):
    if msg['NickName']==GroupName:
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
    def send(self, text):
        self.room.send(text)
    def receive(self):
        return msgs