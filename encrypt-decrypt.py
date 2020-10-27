#pip install pycrypto

from Crypto.Cipher import AES    
from Crypto.Hash import SHA256

password = ("anything")    
hash_obj = SHA256.new(password.encode('utf-8'))    
hkey = hash_obj.digest()

def encrypt(info):
    msg = info
    BLOCK_SIZE = 16
    PAD = "{"
    padding = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PAD
    cipher = AES.new(hkey, AES.MODE_ECB)
    result = cipher.encrypt(padding(msg).encode('utf-8'))
    return result  

msg = "Hello stackoverflow!"
cipher_text = encrypt(msg)
print(cipher_text)

def decrypt(info):
    msg = info
    PAD = "{"
    decipher = AES.new(hkey, AES.MODE_ECB)
    pt = decipher.decrypt(msg).decode('utf-8')
    pad_index = pt.find(PAD)
    result = pt[: pad_index]
    return result

plaintext = decrypt(cipher_text)
print(plaintext)
