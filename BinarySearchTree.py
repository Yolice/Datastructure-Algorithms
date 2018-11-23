import random

class TreeNode():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.parent=None


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
                children.parent=root
        elif data > root.data:
            if root.right:
                self.add(root.right,data)
            else:
                children=TreeNode(data)
                root.right=children
                children.parent=root
        else:
            return False



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

    def FreeNode(self,node):
        node.left=None
        node.right=None
        node.parent=None



    def FindMinNode(self,root):
        if root.left:
            return self.FindMinNode(root.left)
        elif root.left is None:
            return root


    def DeleteTreeNone(self,data):
        node=self.SearchNode(data)
        if node:
            if node.left and node.right and node.data == self.root.data:
                replace_node=self.FindMinNode(node.right)
                replace_node.left=node.left
                replace_node.right=node.right
                replace_node.parent.left=node.parent   ##如果写replace_node.parent=node.parent 即使replacenode的parent是None，但是parent的left依旧链接replacenode，
                                                       ##因为二叉树的特性，replace节点一定是父节点的左子树，所以replacenode.parent.left=None即可以切断链接，最后节点由python回收机制回收
                self.FreeNode(node)
                self.root=replace_node   ##如果删除是根节点，要把代替的节点赋予给根节点





        else:
            return False   ##没有找到节点删除失败




a=BinarySearchTree()

a.CreateBinarySearchTree(30)
a.CreateBinarySearchTree(20)
a.CreateBinarySearchTree(25)
a.CreateBinarySearchTree(24)
a.CreateBinarySearchTree(23)
a.CreateBinarySearchTree(50)
a.CreateBinarySearchTree(35)
a.CreateBinarySearchTree(50)
a.CreateBinarySearchTree(60)
a.CreateBinarySearchTree(70)

a.DeleteTreeNone(30)

a.PreTraversal(a.Get_root())
