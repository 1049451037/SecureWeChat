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
    * [rsa](https://pypi.python.org/pypi/rsa)
    * [hashlib](https://docs.python.org/3/library/hashlib.html?highlight=hashlib#module-hashlib)

# Structure
Three layers.
1. Broadcasting layer. This is provided by ItChat. It can send and receive char stream.
2. P2P layer. Use the services provided by broadcasting layer to achieve P2P protocol. Here we need to build a public key certification service which is independent to wechat.
3. APP layer. Some applications utilizing the functions of P2P layer. For example, we can build a 24h online person to response history message queries. Another example is that besides unicast, we can also consider accomplish multicast, anycast, broadcast(maybe more secure).

