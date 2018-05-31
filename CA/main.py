import itchatmp
import rsa
import pickle

with open('cakey/pri.pem', 'rb') as f:
    prikey = rsa.PrivateKey.load_pkcs1(f.read())

itchatmp.update_config(itchatmp.WechatConfig(
    token='testitchatmp',
    appId = 'wx03b5a10f61d8e884',
    appSecret = '7a0bc25cdf7e0ae71ea4c7df54233366'))

def enc(bytestream):
    return base64.b64encode(bytestream).decode('ascii')
def dec(charstream):
    return base64.b64decode(charstream)

@itchatmp.msg_register(itchatmp.content.TEXT)
def text_reply(msg):
    message = dec(msg['Content'])
    print(pickle.loads(message))
    return enc(rsa.sign(message, prikey, 'SHA-256'))

itchatmp.run()