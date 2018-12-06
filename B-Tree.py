class B_TreeNode:
    def __init__(self,MinValue):
        self.MinValue=MinValue
        self.MaxValue=None
        self.Left=None
        self.Mid=None
        self.Right=None
        self.Parent=None



class B_TreeTempNode:  ##用于复分裂的零时节点
    def __init__(self):
        self.MinValue=None
        self.MidValue=None
        self.MaxValue=None
        self.Left=None
        self.MidLeft=None
        self.MidRight=None
        self.Right=None
        self.Parent=None



class B_Tree:
    def __init__(self):
        self.root=None


    def Fission(self,node):
        pass


    def ReFission(self,node):
        pass


    def Get_root(self):
        return self.root


    def SearchNode(self,data):
        pass


    def SearchStep(self,node,data):
        pass


    def ToFission(self,node):
        if node.Parent and node.Parent.MaxValue:  ##如果父节点有2个值时候需要做复分裂，即分裂值要继续往上传
             self.ReFission()
        else:   ##否则父节点只有一个值，直接把分裂的值塞入父节点的右值即可
             self.Fission()  ##普通分裂时候把传递至根节点考虑进去


    def InsertBTreeNode(self,node,data):  ##默认只有一个值时候值在Min值位置，如果有右值代表有2个值
        if node.MaxValue:      ##如果右值存在
            if data<node.MinValue:
                if node.Left:
                    self.InsertBTreeNode(node.Left,data)
                else:   ##如果根据比较结果没有子节点时,因为此时确认有右值，所以一定会分裂
                    self.ToFission(node)
            elif data>node.MaxValue:
                if node.Rgiht:
                    self.InsertBTreeNode(node.Right,data)
                else:
                    self.ToFission(node)
            else:   ##data介于Min和Max之间
                if node.Mid:
                    self.InsertBTreeNode(node.Mid,data)
                else:
                    self.ToFission(node)
        else: ##此时没有右值，所以可以直接插入
            if data<node.MinValue:
                if node.Left:
                    self.InsertBTreeNode(node.Left,data)
                else:
                    ##直接插入到node的右值，并且sort排序
            elif data>node.MinValue:
                if node.Mid:
                    self.InsertBTreeNode(node.Right,data)
                else:
                    ##直接插入到node的右值，并且sort排序
            else:
                if node.Right:
                    self.InsertBTreeNode(node.Mid, data)
                else:
                    ##直接插入到node的右值，并且sort排序




    def CreateB_Tree(self,data):
        if self.root is None:
            node=B_TreeNode(data)
            self.root=node
        else:
            self.InsertBTreeNode(self.root,data)





