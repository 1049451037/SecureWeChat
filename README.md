# SecureWeChat
Secure point-to-point protocol based on broadcasting network. Group project of Computer Networks course.

# Introduction
This project aims to provide a solution of secure P2P protocol based on broadcasting network. 
We take wechat group as an example. People who join the group can communicate to anyone else in the group. 
Although everyone can see the information sent by anyone, only the target person 
can read valid message and only the real sender and target receiver know who send and receive the message. 
The only thing others know is that the message is not sent to/by him/her.
So we call it a secure P2P protocol based on broadcasting network.

# Environment and Requirements
* Windows or Ubuntu
* Python 3.5+
    * [Itchat](https://github.com/littlecodersh/ItChat)
    * [rsa](https://stuvel.eu/python-rsa-doc/usage.html)
    * [cryptography](https://cryptography.io/en/latest/fernet/)
    * [hashlib](https://docs.python.org/3/library/hashlib.html?highlight=hashlib#module-hashlib)
    * [tkinter](https://docs.python.org/3/library/tkinter.html)

# Structure
## Layers
Three layers.
1. Char stream broadcasting layer. This is provided by ItChat. It can send and receive char stream.
2. Byte stream broadcasting layer. Based on char stream broadcasting layer and bit operation.
3. P2P layer. Use the services provided by byte stream broadcasting layer to achieve P2P protocol. Here we need to build a public key certification service which is independent to wechat.
4. APP layer. Some applications utilizing the functions of P2P layer. Several examples:
    * Build a 24h online person to response history message queries.
    * Accomplish multicast, anycast, broadcast(maybe more secure) besides unicast.
    * GUI interface.
## Services
1. Public key control.
2. Message protocol.
