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
        rooms = itchat.search_chatrooms(GroupName)
        for i in range(len(rooms)):
            print(str(i) +'.', rooms[i]['NickName'])
        id = int(input('找到' + str(len(rooms)) + '个相关群，请输入群编号：'))
        self.room = rooms[id]
        self.room = itchat.update_chatroom(self.room['UserName'], detailedMember=True)
        # myUserName = itchat.get_friends(update=True)[0]["UserName"]
        # print(myUserName)
    def send(self, charstream):
        self.room.send(charstream)
    def receive(self):
        return msgs