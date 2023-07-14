import hashlib

class MerkleTree:
    def __init__(self, leaves):
        self.leaves = leaves
        self.tree = self.build_tree()

    def build_tree(self):
        if len(self.leaves) == 0:
            return []

        tree = [leaf for leaf in self.leaves]

        while len(tree) > 1:
            tree_level = []
            for i in range(0, len(tree), 2):
                left_child = tree[i]
                right_child = tree[i + 1] if i + 1 < len(tree) else tree[i]
        parent_hash = self.hash_children(left_child, right_child)
        tree_level.append(parent_hash)
        tree = tree_level

        return tree[0]

def hash_children(self, left_child, right_child):
        combined_data = left_child + right_child
        combined_hash = hashlib.sha256(combined_data.encode()).hexdigest()
        return combined_hash

# 示例用法
leaves = ["A", "B", "C", "D"]
merkle_tree = MerkleTree(leaves)
root_hash = merkle_tree.tree
print("Root Hash:", root_hash)