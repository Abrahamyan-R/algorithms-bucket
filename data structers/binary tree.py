class BinaryTree:
    class Node:
        def __init__(self, data):
            self.left = None
            self.right = None
            self.data = data

    def __init__(self):
        self.root = None

    def add(self, data):
        new_node = self.Node(data)

        curr = self.root
        while curr:
            if new_node.data == curr.data:
                raise ValueError("Duplicate values does not allowed")
            elif new_node.data > curr.data:
                if not curr.right:
                    curr.right = new_node
                    return
                curr = curr.right
            else:
                if not curr.left:
                    curr.left = new_node
                    return
                curr = curr.left