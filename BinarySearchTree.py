import random

class BinaryTreeNode():
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinarySearchTree():
    def __init__(self):
        self.root=None

    def get_root(self):
        return self.root

    def GenerateBST(self,value):
        if self.root is None:
            self.root=BinaryTreeNode(value)
        else:
            self.InsertNode(self.root,value)

    def InsertNode(self,node,value):
        if value<node.value:
            if node.left is None:
                node.left=BinaryTreeNode(value)
            else:
                self.InsertNode(node.left,value)
        elif value>node.value:
            if node.right is None:
                node.right=BinaryTreeNode(value)
            else:
                self.InsertNode(node.right,value)

    def SearchValue(self,value):
        if self.root is None:
            return None
        else:
            self.SearchStep()

    def SearchStep(self,node,value):
        if node.value==value:
            return node
        elif value<node.value and node.left is not None:
            self.SearchStep(node.left,value)
        elif value>node.value and node.right is not None:
            self.SearchStep(node.right,value)

    def PreTraversal(self,node):
        if node is not None:
            print(node.value)
            self.PreTraversal(node.left)
            self.PreTraversal(node.right)

a=BinarySearchTree()
for i in range(10):
    a.GenerateBST(random.randint(40,60))
a.PreTraversal(a.get_root())
