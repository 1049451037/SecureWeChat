import itchat

itchat.auto_login(True)
myself = itchat.get_friends(update=True)[0]
print(myself)
'''
{'Statues': 0, 'StarFriend': 0, 'SnsFlag': 129, 'MemberList': <ContactList: []>, 'AttrStatus': 0, 'RemarkPYInitial': '', 'Uin': 3048088903, 'HeadImgFlag': 1, 'PYQuanPin': '', 'HideInputBarFlag': 0, 'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=70715123&username=@9455a7c336ac8be8e30189591fd9370d803434ee35ea7d21121953b4e7636544&skey=@crypt_3fec8a73_03b88ab30b26e8ca7e426ae61e3c0327', 'OwnerUin': 0, 'Sex': 1, 'EncryChatRoomId': '', 'KeyWord': '', 'Alias': '', 'ContactFlag': 0, 'DisplayName': '', 'UniFriend': 0, 'RemarkPYQuanPin': '', 'Province': '', 'UserName': '@9455a7c336ac8be8e30189591fd9370d803434ee35ea7d21121953b4e7636544', 'Signature': 'Simplicity is the ultimate sophistication.', 'City': '', 'RemarkName': '', 'NickName': '吕青松', 'MemberCount': 0, 'VerifyFlag': 0, 'ChatRoomId': 0, 'PYInitial': '', 'WebWxPluginSwitch': 0, 'AppAccountFlag': 0}
'''
itchat.logout()

