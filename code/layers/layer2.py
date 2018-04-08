from .layer1 import Broadcasting as bc
import rsa

# https://stuvel.eu/python-rsa-doc/usage.html
# 仍需修改，因为rsa只能加密很短的信息

class P2P(object):
    def __init__(self, groupname):
        self.bottom = bc(groupname)
        self.members = self.bottom.room['MemberList']
    def showmembers(self):
        memberlist = []
        # 'NickName', 'Statues', 'UniFriend', 'Uin', 'RemarkName', 'Signature', 'Alias', 'City', 'DisplayName', 'OwnerUin', 'HideInputBarFlag', 'MemberCount', 'RemarkPYInitial', 'AttrStatus', 'EncryChatRoomId', 'PYQuanPin', 'MemberList', 'KeyWord', 'ContactFlag', 'StarFriend', 'Province', 'UserName', 'Sex', 'SnsFlag', 'PYInitial', 'HeadImgUrl', 'RemarkPYQuanPin', 'ChatRoomId', 'IsOwner', 'AppAccountFlag', 'VerifyFlag'
        for member in self.members:
            memberlist.append(member['UserName']) # print NickName的时候会有编码问题
        return memberlist
    def enc(self, text, pubkey):
        message = text.encode('utf8')
        crypto = rsa.encrypt(message, pubkey)
        L = len(crypto)
        mynews = b''
        for i in range(L):
            for j in range(0, 8, 4):
                thbit = (crypto[i]>>j)&15
                thchar = chr(ord('a')+thbit)
                mynews += thchar.encode('ascii')
        return mynews.decode('ascii')
    def dec(self, msg, prikey):
        news = msg.encode('ascii')
        crypto = []
        for i in range(0, len(news), 2):
            num = 0
            for j in range(2):
                num = (num<<4) | (news[i+1-j]-ord('a'))
            crypto.append(num)
        crypto = bytes(crypto)
        message = rsa.decrypt(crypto, prikey)
        return message.decode('utf8')
    def send(self, text, pubkey):
        self.bottom.send(self.enc(text, pubkey))
    def receive(self, prikey):
        msgs = []
        for msg in self.bottom.receive():
            try:
                msgs.append(self.dec(msg, prikey))
            except Exception as e:
                print(e)
        return msgs