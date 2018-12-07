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


    def Fission(self,node,data): ##单分裂有分裂后的两个叶节点链向None，且上传节点不会造成复分裂
        L=[node.MinValue,node.MaxValue,data]
        L.sort()
        if node == self.root: ##单分裂的root情况只有在一开始会出现
            new_root=B_TreeNode(L[1])
            self.root=new_root
            LeftFission=B_TreeNode(L[0])
            RightFission=B_TreeNode(L[2])
            new_root.Left=LeftFission
            new_root.Right=RightFission
            LeftFission.Parent=new_root
            RightFission.Parent=new_root
        else: ##更一般的单分裂情况,要分开讨论左，右两种情况的节点维护，因为这里是单分裂，上头只能有一个Min值，所以只有左右两种情况
            if node.MinValue < node.Parent.MinValue:  ##此时是左子节点
                L=[node.MinValue,node.MaxValue,data]
                L.sort()
                LeftFission=B_TreeNode(L[0])
                MidFission=B_TreeNode(L[2])
                temp=node.Parent.MinValue
                node.Parent.MinValue=L[1]
                node.Parent.MaxValue=temp
                node.Parent.Left=LeftFission    ##在维护完left mid right后不要忘记维护parent节点
                node.Parent.Mid=MidFission
                LeftFission.Parent=node.Parent
                MidFission.Parent=node.Parent
                node.Parent=None  ##回收垃圾
            elif node.MinValue > node.Parent.MinValue: ##此时是右子节点
                L=[node.MinValue,node.MaxValue,data]
                L.sort()
                MidFission=B_TreeNode(L[0])
                RightFission=B_TreeNode(L[2])
                node.Parent.MaxValue=L[1]
                node.Parent.Mid=MidFission
                node.Parent.Right=RightFission
                MidFission.Parent=node.Parent
                RightFission.Parent=node.Parnet
                node.Parent=None
            else: ##如果值相等在b树是错误的
                return False








    def ReFission(self,node,data):
        pass


    def Get_root(self):
        return self.root


    def SearchNode(self,data):
        pass


    def SearchStep(self,node,data):
        pass


    def GetMax(self,value_1,value_2):
        if value_1>value_2:
            return value_1
        else:
            return value_2

    def ToFission(self,node,data):
        if node.Parent and node.Parent.MaxValue:  ##如果父节点有2个值时候需要做复分裂，即分裂值要继续往上传
             self.ReFission(node,data)
        else:   ##否则父节点只有一个值，直接把分裂的值塞入父节点的右值即可
             self.Fission(node,data)  ##普通分裂时候把传递至根节点考虑进去


    def InsertBTreeNode(self,node,data):  ##默认只有一个值时候值在Min值位置，如果有右值代表有2个值
        if node.MaxValue:      ##如果右值存在
            if data<node.MinValue:
                if node.Left:
                    self.InsertBTreeNode(node.Left,data)
                else:   ##如果根据比较结果没有子节点时,因为此时确认有右值，所以一定会分裂
                    self.ToFission(node,data)
            elif data>node.MaxValue:
                if node.Rgiht:
                    self.InsertBTreeNode(node.Right,data)
                else:
                    self.ToFission(node,data)
            else:   ##data介于Min和Max之间
                if node.Mid:
                    self.InsertBTreeNode(node.Mid,data)
                else:
                    self.ToFission(node,data)
        else: ##此时没有右值，所以可以直接插入
            if data<node.MinValue:
                if node.Left:
                    self.InsertBTreeNode(node.Left,data)
                else:  ##直接插入时要排序左右值以从小到大的顺序排列
                    Max_value=self.GetMax(node.MinValue,data)
                    if Max_value == data:
                        node.MaxValue=data
                    else:
                        node.MaxValue=node.MinValue
                        node.MinValue=data
            elif data>node.MinValue:
                if node.Mid:
                    self.InsertBTreeNode(node.Right,data)
                else:
                    Max_value = self.GetMax(node.MinValue, data)
                    if Max_value == data:
                        node.MaxValue = data
                    else:
                        node.MaxValue = node.MinValue
                        node.MinValue = data

            else:
                if node.Right:
                    self.InsertBTreeNode(node.Mid, data)
                else:
                    Max_value = self.GetMax(node.MinValue, data)
                    if Max_value == data:
                        node.MaxValue = data
                    else:
                        node.MaxValue = node.MinValue
                        node.MinValue = data




    def CreateB_Tree(self,data):
        if self.root is None:
            node=B_TreeNode(data)
            self.root=node
        else:
            self.InsertBTreeNode(self.root,data)






a=B_Tree()

a.CreateB_Tree(1)
