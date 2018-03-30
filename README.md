# SecureWeChat
Secure Point-To-Point protocol based on broadcasting network. Group project of Computer Networks course.

# Introduction
This project aims to provide a solution of secure p2p communicating based on broadcasting network. 
We take wechat group as an example. People who join the group can communicate to anyone else in the group. 
Although everyone can see the information sent by anyone, only the target person 
can read valid message and only sender and receiver know who send and receive the message. 
The only thing others know is that the message is not sent to/by him/her.
So we call it a secure point-to-point protocol based on broadcasting network.

# Environment and Requirements
* Windows or Ubuntu
* Python 3.5+
    * [Itchat](https://github.com/littlecodersh/ItChat)
    * [rsa](https://pypi.python.org/pypi/rsa)
    * [hashlib](https://docs.python.org/3/library/hashlib.html?highlight=hashlib#module-hashlib)

# Structure
Four layers.
1. Wechat layer. This is provided by Itchat.
2. Broadcasting layer. Simulate a broadcasting environment based on Wechat layer.
3. P2P layer. Use the services provided by broadcasting layer to achieve p2p protocol.
4. GUI layer. Complete an application utilizing the functions of P2P layer.

# Optional
Besides unicast, we can also consider accomplish multicast, anycast, broadcast(maybe more secure).
