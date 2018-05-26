from .layer1 import ImageBroadcast as imgbc
from .config import Config
import os
import random
import string
import stepic
from PIL import Image

class ByteStreamBroadcast(object):
    def __init__(self, groupname):
        self.down = imgbc(groupname)
    def random_name(self, size = 6, chars = string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
    def get_a_file_name(self):
        fns = []
        for fn in os.listdir(Config.pre_path + 'download'):
            if fn.find('.') != -1 and fn.split('.')[-1].lower() in set(['jpg', 'jpeg', 'png']):
                fns.append(fn)
        return Config.pre_path + 'download/' + random.choice(fns)
    def enc(self, bytestream):
        fn = self.get_a_file_name()
        hz = fn.split('.')[-1]
        img = Image.open(fn)
        modified = stepic.encode(img, bytestream)
        new_fn = Config.pre_path + 'generated/' + self.random_name() + '.' + hz
        if hz.lower() == 'jpg' or hz.lower() == 'jepg':
            format = 'JPEG'
        else:
            format = 'PNG'
        modified.save(new_fn, format)
        return new_fn
    def dec(self, file_name_of_image):
        img = Image.open(file_name_of_image)
        bytestream = stepic.decode(img)
        return bytestream
    def send(self, bytestream):
        self.down.send(self.enc(bytestream))
    def receive(self):
        msgs = []
        for msg in self.down.receive():
            try:
                msgs.append(self.dec(msg))
            except Exception as e:
                print(e) # 调试时候打印
        return msgs
    def logout(self):
        self.down.logout()

if __name__ == '__main__':
    bsbc = ByteStreamBroadcast('微信测试群')
    bsbc.send(b'hello')
    input()
    for msg in bsbc.receive():
        print(msg.decode('utf8'))