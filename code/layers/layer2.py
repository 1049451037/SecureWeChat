from .layer1 import CharStreamBroadcast as csbc

class ByteStreamBroadcast(object):
    def __init__(self, groupname):
        self.down = csbc(groupname)
        self.room = self.down.room
    def enc(self, bytestream, scale = 4): # scale是把一个字节拆分成几位一组，可以选择的数字有1, 2, 4
        L = len(bytestream)
        filt = 2**scale - 1
        newstream = b''
        for i in range(L):
            for j in range(0, 8, scale):
                thbit = (bytestream[i]>>j)&filt
                thchar = chr(ord('a')+thbit)
                newstream += thchar.encode('ascii')
        return newstream
    def dec(self, charstream, scale = 4): # enc的scale和dec的scale要一致
        newstream = charstream.encode('ascii')
        bytestream = []
        step = 8//scale
        for i in range(0, len(newstream), step):
            num = 0
            for j in range(step):
                num = (num<<scale) | (news[i+step-1-j]-ord('a'))
            bytestream.append(num)
        bytestream = bytes(bytestream)
        return bytestream
    def send(self, bytestream, scale = 4):
        self.down.send(self.enc(bytestream, scale).decode('ascii'))
    def receive(self, scale = 4):
        msgs = []
        for msg in self.down.receive():
            try:
                msgs.append(self.dec(msg, scale))
            except Exception as e:
                print(e) # 调试时候打印
        return msgs