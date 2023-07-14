import hashlib

def rho_sm3(message):
    # 将消息分块
    blocks = [message[i:i+64] for i in range(0, len(message), 64)]
    
    # 初始化初始压缩函数的输入
    h = bytearray.fromhex("7380166f4914b2b972fb8951a8274c60"
                          "986b5fc0e1e25b88c4dd3a367b0e2e8c")
    
    # 对每个块执行初始压缩函数
    for block in blocks:
        # 将当前块与初始压缩函数的输入进行异或运算
        x = bytearray(len(h))
        for i in range(min(len(h), len(block))):
         x[i] = h[i] ^ block[i]
        
        # 执行SM3算法的初始压缩函数
        h = hashlib.new('sm3', x).digest()
    
    return h.hex()

# 测试示例
message = b'Hello, World!'
hash_value = rho_sm3(message)
print("Hash value:", hash_value)