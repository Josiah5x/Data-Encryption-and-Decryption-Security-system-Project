from cryptography.fernet import Fernet
import base64

with open('cv.key', 'rb') as mykey:
    key = mykey.read()

f = Fernet(key)

with open('JOSIAH LIVINUS CHUNTAN CV224.docx', 'rb') as encrypted_files:
    encryted = encrypted_files.read()

decrypt = f.decrypt(encryted) 

with open('JOSIAH LIVINUS CHUNTAN CV224.docx', 'wb') as decrypted_files:
    decrypted_files.write(decrypt)