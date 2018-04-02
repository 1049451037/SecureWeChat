from .layer1 import Broadcasting as bc

class P2P(object):
    def __init__(self, groupname):
        self.bottom = bc(groupname)
        self.members = self.bottom.room['MemberList']
    def showmembers(self):
        memberlist = []
        # 'NickName', 'Statues', 'UniFriend', 'Uin', 'RemarkName', 'Signature', 'Alias', 'City', 'DisplayName', 'OwnerUin', 'HideInputBarFlag', 'MemberCount', 'RemarkPYInitial', 'AttrStatus', 'EncryChatRoomId', 'PYQuanPin', 'MemberList', 'KeyWord', 'ContactFlag', 'StarFriend', 'Province', 'UserName', 'Sex', 'SnsFlag', 'PYInitial', 'HeadImgUrl', 'RemarkPYQuanPin', 'ChatRoomId', 'IsOwner', 'AppAccountFlag', 'VerifyFlag'
        for member in self.members:
            memberlist.append(member['PYQuanPin']) # print NickName的时候会有编码问题……没办法所以就print了拼音
        return memberlist
    def send(self, to, text):
        self.bottom.room.send(u'@%s\u2005%s' % (to, text))
    def receive(self):
        return self.bottom.receive()