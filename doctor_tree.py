
class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, child_name, side):
        """Insert a child under a given parent on the specified side."""
        parent_node = self._find(self.root, parent_name)
        if not parent_node:
            raise ValueError(f"Parent '{parent_name}' not found in tree.")

        new_node = DoctorNode(child_name)

        if side == "left":
            if parent_node.left is None:
                parent_node.left = new_node
            else:
                raise ValueError(f"Parent '{parent_name}' already has a left child.")
        elif side == "right":
            if parent_node.right is None:
                parent_node.right = new_node
            else:
                raise ValueError(f"Parent '{parent_name}' already has a right child.")
        else:
            raise ValueError("Side must be 'left' or 'right'.")

    def _find(self, node, name):
        """Recursive search for a node by name."""
        if node is None:
            return None
        if node.name == name:
            return node
        return self._find(node.left, name) or self._find(node.right, name)

    #Traversals
    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]


#Test 
if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")
    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print(tree.preorder(tree.root))   # ["Dr. Croft", "Dr. Phan", "Dr. Morgan", "Dr. Carson", "Dr. Goldsmith"]
    print(tree.inorder(tree.root))    # ["Dr. Morgan", "Dr. Phan", "Dr. Carson", "Dr. Croft", "Dr. Goldsmith"]
    print(tree.postorder(tree.root))  # ["Dr. Morgan", "Dr. Carson", "Dr. Phan", "Dr. Goldsmith", "Dr. Croft"]
