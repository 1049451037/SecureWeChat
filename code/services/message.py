import json
import rsa

class Message(object):
    def __init__(self):
        pass
    def EncodeMessage(self, arg_dict):
        '''
            to be filled
        '''
        return message # 带有时间戳、数字签名等信息的消息，加密是否在这里进行？
    def DecodeMessage(self, message):
        '''
            to be filled
        '''
        return arg_dict # 解读并验证消息