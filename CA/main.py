import itchatmp
import rsa
import pickle

with open('cakey/pri.pem', 'rb') as f:  # 私钥也不传到github了
    prikey = rsa.PrivateKey.load_pkcs1(f.read())

itchatmp.update_config(itchatmp.WechatConfig(
    token='testitchatmp',
    appId = 'wx03b5a10f61d8e884',
    appSecret = '7a0bc25cdf7e0ae71ea4c7df54233366'))  # 这些信息就不传到github了，属于隐秘信息

def enc(bytestream, scale = 4): # scale是把一个字节拆分成几位一组，可以选择的数字有1, 2, 4
    L = len(bytestream)
    filt = 2**scale - 1
    newstream = b''
    for i in range(L):
        for j in range(0, 8, scale):
            thbit = (bytestream[i]>>j)&filt
            thchar = chr(ord('a')+thbit)
            newstream += thchar.encode('ascii')
    return newstream.decode('ascii')
def dec(charstream, scale = 4): # enc的scale和dec的scale要一致
    newstream = charstream.encode('ascii')
    bytestream = []
    step = 8//scale
    for i in range(0, len(newstream), step):
        num = 0
        for j in range(step):
            num = (num<<scale) | (newstream[i+step-1-j]-ord('a'))
        bytestream.append(num)
    bytestream = bytes(bytestream)
    return bytestream

@itchatmp.msg_register(itchatmp.content.TEXT)
def text_reply(msg):
    message = dec(msg['Content'])
    print(pickle.loads(message))
    return enc(rsa.sign(message, prikey, 'SHA-256'))

itchatmp.run()