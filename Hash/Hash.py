import List

class HashTable: ##一个长度为求余数长的数组，数组每个元素值有一个head链表头，可以把哈希冲突的值写进链表，在O（1）后有O（n）的查找
    def __init__(self,length):
        self.Table_Length=length
        self.lastnode=None


    def Hash(self,key,length):##hash函数返回地址，用求余来分配值
        return key%length ##默认哈希表分割为0-9空位来存放值


    def Initial_Hash(self,length):
        Table=[List.List() for i in range(length)]
        for i,j in zip(Table,range(len(Table))):
            i.Insert(j)
        return Table



    def Insert(self,value,Table):
        addr=self.Hash(value,self.Table_Length)
        new_node=List.ListNode(value)
        if Table[addr].head.next==None: ##只有第一次head后面为None时候，lastnode才和head指向一起
            self.last_node = Table[addr].head
        self.last_node.next=new_node
        self.last_node=new_node




    def Get_length(self):
        return self.Table_Length



    def Search(self,value,Table):
        addr=self.Hash(value,self.Table_Length)
        node=Table[addr].head
        while node.data != value and node.next!=None:
            node=node.next
        if node.data == value:
            return True
        else:
            return False



    def Remove(self,value,Table):
        flag=self.Search(value,Table)
        if flag == False:
            print("值不存在，删除失败")
            return False
        else:
            addr=self.Hash(value,self.Table_Length)
            heads=Table[addr].head
            if value==heads.data:
                Table[addr].head=Table[addr].head.next
            else:
                while heads and heads.next.data!=value:
                    heads=heads.next
                if heads:
                    heads.next=heads.next.next
                else:
                    return False


















'''
a=HashTable(10)
Table=a.Initial_Hash(a.Get_length())
a.Insert(20,Table)
a.Remove(20,Table)
a.Insert(30,Table)
a.Insert(40,Table)
print(a.Search(30,Table))
'''
