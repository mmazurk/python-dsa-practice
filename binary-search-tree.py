
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node(value={self.val}, left={self.left is not None}, right={self.right is not None})"


class Bst:
    def __init__(self, root=None):
        self.root = root

    def insert(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if new_node.val < current_node.val:
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        current_node.left = new_node
                        break
                elif new_node.val > current_node.val:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node.right = new_node
                        break
                else:
                    return "error -- duplicate node"

    def find(self, val):
        if self.root is None:
            return "This tree is empty"
        else:
            target_val = val
            current_node = self.root
            while current_node:
                if target_val == current_node.val:
                    return current_node
                elif target_val < current_node.val:
                    current_node = current_node.left
                else:  # target_val > current_node.val
                    current_node = current_node.right
            return "Node is not in this tree"


mbst = Bst()
mbst.insert(10)
mbst.insert(20)
mbst.insert(5)
mbst.insert(30)
node = mbst.find(20)
print(node)
