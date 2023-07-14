import hashlib

def length_extension_attack(hash_func, original_message, original_hash, extension_data):
    # 获取原始消息的长度
    original_length = len(original_message)

    # 构造填充数据
    padding = b'\x80' + b'\x00' * ((64 - (original_length + 8) % 64) % 64)
    length_bits = (original_length + len(padding) + 8) * 8
    padding += length_bits.to_bytes(8, 'big')

    # 计算新消息的哈希值
    hash_obj = hash_func()
    hash_obj.update(extension_data + padding)
    new_hash = hash_obj.digest()

    return new_hash.hex()

# 示例使用SHA256哈希函数进行长度扩展攻击
original_message = b'Original Message'
extension_data = b'Extension Data'

# 计算原始消息的哈希值
original_hash = hashlib.sha256(original_message).digest()

# 进行长度扩展攻击
new_hash = length_extension_attack(hashlib.sha256, original_message, original_hash, extension_data)

print("Original Hash:", original_hash.hex())
print("New Hash:", new_hash)