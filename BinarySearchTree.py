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
            if node.left and node.right:   ##假如要删除的节点左右子树都存在的情况
                replace_node=self.FindMinNode(node.right)
                replace_node.left=node.left
                replace_node.right=node.right
                if node.data == self.root.data:            ##要删除的是根节点的情况
                    replace_node.parent.left=None          ##如果写replace_node.parent=None,那么parent的left依旧链接replacenode，所以要写出parent.left链向目标
                                                           ##因为二叉树的特性，replace节点一定是父节点的左子树，所以replacenode.parent.left=None即可以切断链接，最后节点由python回收机制回收
                    self.FreeNode(node)
                    self.root=replace_node                 ##如果删除是根节点，那么代替节点就是新的根节点

                else:                                      ##在删除之前要找到被删除点是左子树或者是右子树
                    if node.parent.left and node.parent.left.data == node.data:
                        replace_node.parent.left=None
                        node.parent.left=replace_node
                        self.FreeNode(node)
                    elif node.parent.right and node.parent.right.data == node.data:
                        replace_node.parent.left=None
                        node.parent.right=replace_node
                        self.FreeNode(node)
            elif node.left and node.right is None:   ##只有单一左子树存在时候
                if node.parent.left and node.parent.left.data == node.data:   ##判断左子树或者右紫薯
                    node.parent.left=node.left
                    self.FreeNode(node)
                elif node.parent.right and node.parent.right.data == node.data:
                    node.parent.right=node.left
                    self.FreeNode(node)
            elif node.right and node.left is None:
                if node.parent.left and node.parent.left.data == node.data:
                    node.parent.left=node.right
                    self.FreeNode(node)
                elif node.parent.right and node.parent.right.data == node.data:
                    node.parent.right=node.right
                    self.FreeNode(node)
            elif node.left is None and node.right is None:  ##如果没有左右子树
                if node.parent.left and node.parent.left.data == node.data:
                    node.parent.left=None
                    self.FreeNode(node)
                elif node.parent.right and node.parent.right.data == node.data:
                    node.parent.right=None
                    self.FreeNode(node)
        else:
            return False   ##没有找到节点删除失败




a=BinarySearchTree()

a.CreateBinarySearchTree(62)
a.CreateBinarySearchTree(58)
a.CreateBinarySearchTree(88)
a.CreateBinarySearchTree(47)
a.CreateBinarySearchTree(73)
a.CreateBinarySearchTree(99)
a.CreateBinarySearchTree(35)
a.CreateBinarySearchTree(51)
a.CreateBinarySearchTree(93)
a.CreateBinarySearchTree(29)
a.CreateBinarySearchTree(37)
a.CreateBinarySearchTree(49)
a.CreateBinarySearchTree(56)
a.CreateBinarySearchTree(36)
a.CreateBinarySearchTree(48)
a.CreateBinarySearchTree(50)


print(a.DeleteTreeNone(36))

a.PreTraversal(a.Get_root())
