from .config import Config
import itchat
from itchat.content import *
import io

GroupName = '微信测试群'
msgs = []

@itchat.msg_register(PICTURE, isGroupChat=True)
def download_file(msg):
    fn = Config.pre_path + 'download/' + msg.fileName
    msg.download(fn)
    msgs.append(fn) # 如何判断仅属于GroupName的消息才接收？或者是否需要这样的判断？

class ImageBroadcast(object):
    def __init__(self, groupname):
        itchat.auto_login(True)
        global GroupName
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
    def send(self, img_file_name): # image file name
        '''
        这里本来也可以传入图片的二进制的，但是这个方法itchat有个bug，就是gif图片会变成静态的，所以就改成用文件名了，所以可能需要在本地中转一下
        '''
        self.room.send_file(img_file_name)
        msgs.append(img_file_name)
    def receive(self): # return a list of file names of images
        '''
        因为itchat收到图片以后会自动保存到本地，因此这个函数返回文件名列表
        '''
        return msgs
    def logout(self):
        itchat.logout()

if __name__ == '__main__':  # 测试程序
    ib = ImageBroadcast('微信测试群')
    ib.send('./download/pic.png')
    input()
    print(ib.receive())