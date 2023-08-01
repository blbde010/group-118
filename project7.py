import hashlib

class GeneralizedHashChain:
    def __init__(self):
        self.chain = []

    def add_element(self, element):
        if len(self.chain) == 0:
            self.chain.append(element)
        else:
           
            previous_hash = self.get_last_hash()
            new_hash = hashlib.sha256((previous_hash + element).encode()).hexdigest()
            self.chain.append(new_hash)

    def get_last_hash(self):
        return self.chain[-1]
    
    def verify_chain(self):
        for i in range(1, len(self.chain)):
            previous_hash = self.chain[i-1]
            current_element = self.chain[i]
            computed_hash = hashlib.sha256((previous_hash + current_element).encode()).hexdigest()
            if computed_hash != current_element:
                return False
        return True

# 示例用法
chain = GeneralizedHashChain()
chain.add_element("test1")
chain.add_element("test2")
chain.add_element("test3")

print("hash链", chain.chain)
print("最终hash值:", chain.get_last_hash())
print("正确性", chain.verify_chain())