from cryptography.fernet import Fernet

with open('cv.key', 'rb') as cvkey:
    key = cvkey.read()

f = Fernet(key)

with open('JOSIAH LIVINUS CHUNTAN CV224.docx', 'rb') as original_files:
    original = original_files.read()

encrypted = f.encrypt(original)

with open('JOSIAH LIVINUS CHUNTAN CV224.docx', 'wb') as encrypted_files:
    encrypted_files.write(encrypted)
