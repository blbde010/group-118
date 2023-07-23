import struct
import numpy as np


def rotate_left(x, n):
    return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF


def padding(message):
    ml = len(message) * 8
    message += b'\x80'
    message += b'\x00' * ((56 - len(message) % 64) % 64)
    message += struct.pack('>Q', ml)
    return message


def sm3(message):
    message = padding(message)
    h = [0x7380166F, 0x4914B2B9, 0x172442D7, 0xDA8A0600,
         0xA96F30BC, 0x163138AA, 0xE38DEE4D, 0xB0FB0E4E]

    for i in range(0, len(message), 64):
        w = list(struct.unpack('>16I', message[i:i+64]))

        # 循环展开（我也不知道改来改去还有没有循环展开）
        for j in range(16, 64):
            w.append(
 rotate_left(w[j-16] ^ w[j-9] ^ (rotate_left(w[j-3], 15)), 1) ^ (rotate_left(w[j-13], 7)) ^ w[j-6]
            )
            w.append(
 rotate_left(w[j-15] ^ w[j-8] ^ (rotate_left(w[j-2], 15)), 1) ^ (rotate_left(w[j-12], 7)) ^ w[j-5]
            )
            w.append(
 rotate_left(w[j-14] ^ w[j-7] ^ (rotate_left(w[j-1], 15)), 1) ^ (rotate_left(w[j-11], 7)) ^ w[j-4]
            )
            w.append(
 rotate_left(w[j-13] ^ w[j-6] ^ (rotate_left(w[j], 15)), 1) ^ (rotate_left(w[j-10], 7)) ^ w[j-3]
            )

        
        
        
        

        

    return ''.join([format(x, '08x') for x in h])


# 测试
message = b'Hello, world!'
hash_value = sm3(message)
print(hash_value)
