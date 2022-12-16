import rsa
# import hashlib
from rsa.key import PublicKey, PrivateKey
msg = 'hello bro'

publickey, privatekey = rsa.newkeys(512)
print(publickey, privatekey)

ecrypt_msg = rsa.encrypt(msg.encode(), publickey)
print(ecrypt_msg)

dcrypt_msg = rsa.encrypt(ecrypt_msg, Privatekey).decode()
print(dcrypt_msg)