import hashlib
import random

def range_proof(min_value, max_value):
    # 步骤2：在范围内生成一个机数
    r = random.randint(min_value, max_value)

    # 步骤3计算哈希值
    hasi = hashlib.sha256(str(r).encode()).hexdigest()
    print(hasi)
    # 步骤4：将数据发送给验证者
    return r, hasi

def verify_range_proof(min_value, max_value, r, h):
    #重新计算哈希值
    h_prime = hashlib.sha256(str(r).encode()).hexdigest()
    print(h_prime)
    # tset
    if min_value <= r <= max_value and h == h_prime:
        return True
    else:
        return False

# Example 
min_value = 0
max_value = 100
r, h = range_proof(min_value, max_value)
is_valid = verify_range_proof(min_value, max_value, r, h)
print("范围有效:", is_valid)