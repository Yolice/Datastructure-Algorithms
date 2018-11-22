import random

class TreeNode():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None



class BinarySearchTree():
    def __init__(self):
        self.root=None



    def InitRoot(self,data):
        if self.root is None:
            self.root=TreeNode(data)
            return self.root



    def CreateBinarySearchTree(self,data):
        if self.root is None:
            self.InitRoot(data)
        else:
            self.add(self.root,data)



    def Get_root(self):
        return self.root



    def add(self,root,data):
        if data < root.data:
            if root.left:
                self.add(root.left,data)
            else:
                children=TreeNode(data)
                root.left=children
        elif data > root.data:
            if root.right:
                self.add(root.right,data)
            else:
                children=TreeNode(data)
                root.right=children



    def SearchNode(self,data):
        if self.root is None:
            return False
        else:
            return self.SearchStep(self.root,data)      ##从这行开始，到下面searchstep函数都需要return接力返回结果，递归后的函数如果没有return默认返回None


    def SearchStep(self,root,data):
        if root.data == data:
            return root
        elif data < root.data and root.left is not None:
            return self.SearchStep(root.left,data)         ##必须要return
        elif data > root.data and root.right is not None:
            return self.SearchStep(root.right,data)    ##必须要return



    def PreTraversal(self,root):
        if root:
            print(root.data)
            self.PreTraversal(root.left)
            self.PreTraversal(root.right)



    def MidTraversal(self,root):
        if root:
            self.MidTraversal(root.left)
            print(root.data)
            self.MidTraversal(root.left)



    def RearTraversal(self,root):
        if root:
            self.RearTraversal(root.left)
            self.RearTraversal(root.right)
            print(root.data)

    def FindMaxNode(self,root):
        if root.right:
            return self.FindMaxNode(root.right)   ##树是一种递归性质的结构，所以在获取树中的一个节点时候要接力return的值
        elif root.right is None:
            return root



    def FindMinNode(self,root):
        if root.left:
            return self.FindMinNode(root.left)
        elif root.left is None:
            return root



    def DeleteTreeNone(self,data):
        IndexNode=self.SearchNode(data)
        if IndexNode is None:
            print("No such tree node")
        else:
            if IndexNode.left and IndexNode.right:
                replace_node=self.FindMinNode(IndexNode.right)
                replace_node.left=IndexNode.left
                replace_node.right=IndexNode.right
                IndexNode=None
                replace_node=None
            elif IndexNode.left is None and IndexNode.right:
                IndexNode=IndexNode.right
            elif IndexNode.left and IndexNode.right is None:
                IndexNode=IndexNode.left
            else:
                IndexNode=None






a=BinarySearchTree()

for i in range(10):
    a.CreateBinarySearchTree(i)


a.DeleteTreeNone(4)
a.PreTraversal(a.Get_root())
