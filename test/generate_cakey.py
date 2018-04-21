import rsa

(pubkey, prikey) = rsa.newkeys(512)
with open('pub.pem', 'wb') as f:
    f.write(pubkey.save_pkcs1())
with open('pri.pem', 'wb') as f:
    f.write(prikey.save_pkcs1())
with open('pub.pem', 'rb') as f:
    print(len(f.read()))
with open('pri.pem', 'rb') as f:
    print(len(f.read()))
