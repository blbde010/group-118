from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import binascii
key = binascii.unhexlify('0123456789abcdeffedcba9876543210')       
mingwen = b"SDU GAI"
cipher = Cipher(algorithms.SM4(key), modes.ECB())
encryptor = cipher.encryptor()
#填充
padder = padding.PKCS7(128).padder()
padded_result = padder.update(mingwen) + padder.finalize()
#加密
miwen = encryptor.update(padded_result) + encryptor.finalize()
#解密并还原
decryptor = cipher.decryptor()
padded_result = decryptor.update(miwen) + decryptor.finalize()
unpadder = padding.PKCS7(128).unpadder()
result = unpadder.update(padded_result) + unpadder.finalize()
print('明文：', mingwen)
print('密文：', miwen.hex())
print('解密结果：', result)
