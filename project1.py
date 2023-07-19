import random
import time
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def naive_birthday_attack():
    k = 16  # 消息空间大小，选择适当的值
    hash_values = {}  # 存储已计算的哈希值
    
    while True:
        message = generate_random_message(k)  # 生成随机消息
        
        hash_value = calculate_sm3_hash(message.encode())  # 计算哈希值
       
        
        if hash_value in hash_values:
            collision_message = hash_values[hash_value]
            print("Collision found!")
            print("Message 1:", collision_message)
            print("Message 2:", message)
            
            return collision_message, message
        
        hash_values[hash_value] = message

def calculate_sm3_hash(message):
    sm3_hash = hashes.Hash(hashes.SM3(), backend=default_backend())
    sm3_hash.update(message)
    digest = sm3_hash.finalize()
    return digest.hex()

def generate_random_message(k):
    # 生成随机消息，长度为k位
    message = ''.join(random.choices(['0', '1'], k=k))
    return message

# 执行生日攻击
start_time = time.time()
collision_message, message = naive_birthday_attack()
end_time = time.time()
print("Time elapsed:", end_time - start_time, "seconds")
