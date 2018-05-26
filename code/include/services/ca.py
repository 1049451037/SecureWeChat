from .calayers.calayer2 import ByteStreamCA as bsca
from .keys import GetKey
import time
import pickle
import rsa
import tkinter as tk
from tkinter import ttk
from tkinter import *
jm = tk.Tk()
jm.title("SecureWeChat")
def GetCertificate(name):
    gk = GetKey()
    try:
        with open('cert/cert.pkl', 'rb') as f:
            cert = f.read()
        with open('cert/cert_sig', 'rb') as f:
            cert_sig = f.read()
        ca_pubkey = rsa.PublicKey.load_pkcs1(gk.get_ca_pubkey())
        if rsa.verify(cert, cert_sig, ca_pubkey):
            return
    except:
        pass
    tex = "这是你第一次来到这里，你将要做的是一件非常神圣的事情，" \
          "那就是公钥认证目前唯一的公钥认证。是一个叫做smallcoder的公众号，" \
          "所以在认证之前要先关注这个公众号。请保证你输入的是准确的，以保证你与好友的安全交流"
    txt = ttk.Label(jm, text=tex, width=120, wraplength=680, anchor='w')
    txt.grid(column=0, row=0)

    def clickMe():
        act.configure(text="认证中")
        global act2
        global act3
        global act4
        act2 = ttk.Button(jm, text="姓名", command=clickMe1)
        act2.grid(column=1, row=1)
        act3 = ttk.Button(jm, text="性别", command=clickMe2)
        act3.grid(column=1, row=2)
        act4 = ttk.Button(jm, text="邮箱", command=clickMe3)
        act4.grid(column=1, row=3)
        global name
        global sex
        global mail
        name = tk.StringVar()
        nameEntered = ttk.Entry(jm, width=12, textvariable=name)
        nameEntered.grid(column=0, row=1)

        sex = tk.StringVar()
        nameEntered2 = ttk.Entry(jm, width=12, textvariable=sex)
        nameEntered2.grid(column=0, row=2)

        mail= tk.StringVar()
        nameEntered3 = ttk.Entry(jm, width=12, textvariable=mail)
        nameEntered3.grid(column=0, row=3)


    def clickMe1():
        #act2.configure(text='你好，' + name.get() + '先生！')
        act2.configure(text="姓名输入完成")
        act2.configure(state='disabled')

    def clickMe2():
        act3.configure(text="性别输入完成")

    def clickMe3():
        act4.configure(text="邮箱输入完成")
        dic = {'name': name, 'sex': sex, 'mail': mail, 'key': gk.get_self_pubkey()}
        message = pickle.dumps(dic)
        mylayer.send(message)
        time.sleep(5)
        signature = mylayer.receive()[0]
        ca_pubkey = rsa.PublicKey.load_pkcs1(gk.get_ca_pubkey())
        if rsa.verify(message, signature, ca_pubkey):
            with open('cert/cert.pkl', 'wb') as f:
                f.write(message)
            with open('cert/cert_sig', 'wb') as f:
                f.write(signature)
            trust = {gk.get_self_pubkey(): dic}
            with open('trust.pkl', 'wb') as f:
                pickle.dump(trust, f)

        txt = ttk.Label(jm, text=tex, width=120, wraplength=680, anchor='w')
        txt.grid(column=0, row=6)
        mylayer.logout()

    act = ttk.Button(jm, text="现在开始认证", command=clickMe)
    act.grid(column=1, row=0)
    mylayer = bsca(name)
    tex = "恭喜你认证成功！之所以认证如此顺利，是因为目前认证机构仍处于调试阶段，" \
          "所以并不会对你输入的信息真实性做核查." \
          "现在仍然要提醒一下，请保护好你本地的cert文件夹，这个文件夹是你在这里身份的标识，不要上传到网络." \
          "初始的时候你的好友列表里只有你自己，如果想跟他人聊天，可以通过广播自己的公钥来让别人知道你的存在."

    jm.mainloop()


