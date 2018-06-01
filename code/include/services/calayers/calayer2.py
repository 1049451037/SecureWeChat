from .calayer1 import CharStreamCA as csca
import base64

class ByteStreamCA(object):
    def __init__(self, caname):
        self.down = csca(caname)
    def enc(self, bytestream):
        return base64.b64encode(bytestream).decode('ascii')
    def dec(self, charstream):
        return base64.b64decode(charstream)
    def send(self, bytestream):
        self.down.send(self.enc(bytestream))
    def receive(self):
        msgs = []
        for msg in self.down.receive():
            try:
                msgs.append(self.dec(msg))
            except Exception as e:
                pass
        return msgs
    def logout(self):
        self.down.logout()