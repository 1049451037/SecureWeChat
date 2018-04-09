from .layer2 import ByteStreamBroadcast as bsbc
import rsa

# https://stuvel.eu/python-rsa-doc/usage.html
# 仍需修改，因为rsa只能加密很短的信息

class P2P(object):
    def __init__(self, groupname):
        self.down = bsbc(groupname)
        self.members = self.down.room['MemberList']
    def showmembers(self):
        memberlist = []
        # 'NickName', 'Statues', 'UniFriend', 'Uin', 'RemarkName', 'Signature', 'Alias', 'City', 'DisplayName', 'OwnerUin', 'HideInputBarFlag', 'MemberCount', 'RemarkPYInitial', 'AttrStatus', 'EncryChatRoomId', 'PYQuanPin', 'MemberList', 'KeyWord', 'ContactFlag', 'StarFriend', 'Province', 'UserName', 'Sex', 'SnsFlag', 'PYInitial', 'HeadImgUrl', 'RemarkPYQuanPin', 'ChatRoomId', 'IsOwner', 'AppAccountFlag', 'VerifyFlag'
        for member in self.members:
            memberlist.append(member['UserName']) # print NickName的时候会有编码问题
        return memberlist
    def send(self, text, pubkey):
        message = text.encode('utf8')
        crypto = rsa.encrypt(message, pubkey)
        self.down.send(crypto)
    def receive(self, prikey):
        msgs = []
        for msg in self.down.receive():
            try:
                msgs.append(rsa.decrypt(crypto, prikey).decode('utf8'))
            except Exception as e:
                print(e) # 调试时候打印
        return msgs