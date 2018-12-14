'''
没写完的代码，不供参考
'''



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


    def Fission(self,node,insert_node): ##单分裂有分裂后的两个叶节点链向None，且上传节点不会造成复分裂
        if node == self.root: ##单分裂的root情况在一开始或者复分裂到root时候出现
            L = [node.MinValue, node.MaxValue, insert_node.MinValue]
            L.sort()
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
                L=[node.MinValue,node.MaxValue,insert_node.MinValue]
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
                L=[node.MinValue,node.MaxValue,insert_node.MinValue]
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



    def NodeTransformation(self,node):  ##
        pass








    def ReFission(self,node,insert_node):
        if node.Parent == self.root:  ##此时节点Parent有右值且为root节点时候，做一次节点变换就可以退出分裂
            pass

        else: ##如果node.Parent不是root，那么node.Parent.Parent一定会存在
            if node.MinValue < node.Parent.MinValue:  ## 当是其左子节点情况
                L = [node.MinValue, node.MaxValue, insert_node]
                L.sort()
                GrandParent=node.Parent.Parent
                TempNode = B_TreeTempNode()
                TempNode.MinValue = L[1]
                TempNode.MidValue = node.Parent.MinValue
                TempNode.MaxValue = node.Parent.MaxValue
                TempNode.Left = L[0]
                TempNode.MidLeft = L[2]
                TempNode.MidRight = node.Parent.Mid
                TempNode.Right = node.Parent.Right
                ControlNode=self.NodeTransformation(TempNode)
                self.InsertBTreeNode(GrandParent,ControlNode)  ##从self.InsertBTreeNode递归，递归从node=root时候退出
            elif node.MinValue > node.Parent.MinValue and node.MinValue < node.Parent.MaxValue:  ##当是其中子节点情况
                pass
            elif node.MinValue > node.Parent.MaxValue:  ##当是其右子节点情况
                pass



    def Get_root(self):
        return self.root



    def GetMax(self,value_1,value_2):
        if value_1>value_2:
            return value_1
        else:
            return value_2

    def ToFission(self,node,insert_node): ##node是要被插入的地方的点，insert_node是要插入的点
        if node.Parent and node.Parent.MaxValue:  ##如果父节点有2个值时候需要做复分裂，即分裂值要继续往上传
             self.ReFission(node,insert_node)
        else:   ##否则父节点只有一个值，直接把分裂的值塞入父节点的右值即可
             self.Fission(node,insert_node)  ##普通分裂时候把传递至根节点考虑进去


    def InsertBTreeNode(self,node,insert_node):  ##默认只有一个值时候值在Min值位置，如果有右值代表有2个值
        if node.MaxValue:      ##如果右值存在
            if insert_node.MinValue<node.MinValue:
                if node.Left:
                    self.InsertBTreeNode(node.Left,insert_node)
                else:   ##如果根据比较结果没有子节点时,因为此时确认有右值，所以一定会分裂
                    self.ToFission(node,insert_node)
            elif insert_node.MinValue>node.MaxValue:
                if node.Rgiht:
                    self.InsertBTreeNode(node.Right,insert_node)
                else:
                    self.ToFission(node,insert_node)
            else:   ##insert_node介于Min和Max之间
                if node.Mid:
                    self.InsertBTreeNode(node.Mid,insert_node)
                else:
                    self.ToFission(node,insert_node)
        else: ##此时没有右值，所以可以直接插入
            if insert_node.MinValue<node.MinValue:
                if node.Left:
                    self.InsertBTreeNode(node.Left,insert_node)
                else:  ##直接插入时要排序左右值以从小到大的顺序排列
                    Max_value=self.GetMax(node.MinValue,insert_node.MinValue)
                    if Max_value == insert_node.MinValue:
                        node.MaxValue=insert_node.MinValue
                    else:
                        node.MaxValue=node.MinValue
                        node.MinValue=insert_node.MinValue
            elif insert_node.MinValue>node.MinValue:
                if node.Mid:
                    self.InsertBTreeNode(node.Right,insert_node)
                else:
                    Max_value = self.GetMax(node.MinValue, insert_node.MinValule)
                    if Max_value == insert_node.MinValue:
                        node.MaxValue = insert_node.MinValue
                    else:
                        node.MaxValue = node.MinValue
                        node.MinValue = insert_node.MinValue

            else:
                if node.Right:
                    self.InsertBTreeNode(node.Mid, insert_node)
                else:
                    Max_value = self.GetMax(node.MinValue, insert_node.MinValue)
                    if Max_value == insert_node.MinValue:
                        node.MaxValue = insert_node.MinValue
                    else:
                        node.MaxValue = node.MinValue
                        node.MinValue = insert_node.MinValue




    def CreateB_Tree(self,data):
        if self.root is None:
            node=B_TreeNode(data)
            self.root=node
        else:
            insert_node=B_TreeNode(data)
            self.InsertBTreeNode(self.root,insert_node)






a=B_Tree()

a.CreateB_Tree(1)
