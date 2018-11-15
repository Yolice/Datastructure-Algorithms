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

    def FindMin(self,node):
        if node.left:
            return self.FindMin(node.left)
        else:
            return node

    def FindMax(self,node):
        if node.right:
            return self.FindMax(node.right)
        else:
            return node

    def DeleteNode(self,node,value):
        if self.root is None:
            return
        if value<node.value:
            self.DeleteNode(node.left,value)
        if value>node.value:
            self.DeleteNode(node.right,value)
        else:
            if node.left and node.right:
                new_node=self.FindMin(node)
                node.value=new_node.value
                node.right=self.DeleteNode(node.right,new_node.value)
            elif node.left is None and node.right is None:
                node=None
            elif node.left is None:
                node=node.right
            elif node.right is None:
                node=node.left

a=BinarySearchTree()
for i in range(10):
    a.GenerateBST(i)
print(a.FindMin(a.get_root()))
