import itchat
import rsa

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
        self.members = self.room['MemberList']
    def showmembers(self):
        memberlist = []
        for member in self.members:
            memberlist.append(member['UserName'])
        return memberlist
    def send(self, charstream):
        self.room.send(charstream)
    def receive(self):
        return msgs

csbc = CharStreamBroadcast('微信测试群')
usernames = csbc.showmembers()
for un in usernames:
    (pubkey, prikey) = rsa.newkeys(512)
    with open(un + '_pub.pem', 'wb') as f:
        f.write(pubkey.save_pkcs1())
    with open(un + '_pri.pem', 'wb') as f:
        f.write(prikey.save_pkcs1())