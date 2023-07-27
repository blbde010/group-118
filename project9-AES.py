from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def aes_jiami(mingwen, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_ming = pad(mingwen.encode(), AES.block_size)
    miwen_result = cipher.encrypt(padded_ming)
    return base64.b64encode(miwen_result).decode()

def aes_jiemi(miwen, key):
    cipher = AES.new(key, AES.MODE_ECB)
    miwen_de = base64.b64decode(miwen)
    jiemi_ = cipher.decrypt(miwen_de)
    result_ = unpad(jiemi_, AES.block_size)
    return result_.decode()

# 测试
key = b'Sixteen byte key'
mingwen = 'SDU'
miwen = aes_jiami(mingwen, key)
result = aes_jiemi(miwen, key)

print('明文为：', mingwen)
print('密文为：', miwen)
print('解密得到的：', result)