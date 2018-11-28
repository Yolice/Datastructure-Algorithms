class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.bf=None
        self.height=None
        self.parent=None


class Self_Balance_BST:
    def __init__(self):
        self.root=None
        self.balance_fator=[1,0,-1]
        self.count=1
        self.height=0


    def Get_root(self):
        return self.root


    def Create_SelfBalanceTree(self,data):
        if self.root is None:
            self.root=TreeNode(data)
        else:
            self.add_node(self.root,data)


    def add_node(self,root,data):
        if data < root.data :
            if root.left:
                self.add_node(root.left,data)
            else:
                children=TreeNode(data)
                children.parent=root
                root.left=children

        elif data > root.data:
            if root.right:
                self.add_node(root.right,data)
            else:
                children=TreeNode(data)
                children.parent=root
                root.right=children
        else:
            return False


    def CheckBF(self,root):
        if root:
            print(self.Get_node_balancefator(root,self.count))
            self.CheckBF(root.left)
            self.CheckBF(root.right)




    def Get_node_balancefator(self,root,count):
        if root:     ##一切建立在这个节点是存在的情况下
            leftheight=self.PrintHeight(root.left,count)
            self.height=0
            rightheight=self.PrintHeight(root.right,count)
            if leftheight is None and rightheight is None:
                return 0
            elif leftheight is None and rightheight:
                leftheight=0
            elif rightheight is None and leftheight:
                rightheight=0
            return leftheight-rightheight


    def PrintHeight(self,root,count):   ##函数在递归回归到前一个函数的的时候，当前保存的count值正好对应当前高度值。
        if root:
            if count > self.height:
                self.height=count
            self.PrintHeight(root.left,count+1)
            self.PrintHeight(root.right,count+1)
            return self.height        ##这里没有在递归函数上写return是因为不用接力回归的值，此时函数执行到最后必有一个return不像之前查值时候用if分割了3总情况


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





a=Self_Balance_BST()

a.Create_SelfBalanceTree(62)
a.Create_SelfBalanceTree(58)
a.Create_SelfBalanceTree(88)
a.Create_SelfBalanceTree(47)
a.Create_SelfBalanceTree(73)
a.Create_SelfBalanceTree(99)
a.Create_SelfBalanceTree(35)
a.Create_SelfBalanceTree(51)
a.Create_SelfBalanceTree(93)
a.Create_SelfBalanceTree(29)
a.Create_SelfBalanceTree(37)
a.Create_SelfBalanceTree(49)
a.Create_SelfBalanceTree(56)
a.Create_SelfBalanceTree(36)
a.Create_SelfBalanceTree(48)
a.Create_SelfBalanceTree(50)

a.CheckBF(a.Get_root())
