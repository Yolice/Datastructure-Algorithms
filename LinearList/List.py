class ListNode():
    def __init__(self,data):
        self.data=data
        self.next=None

class DoubleListNode():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.rear=None


class List():
    def __init__(self):
        self.head=None
        self.list_head=None

    def Get_Head(self):
        return self.head

    def PreInsert(self,data):
        if self.head is None:
            self.head=ListNode(data)
        else:
            new_node=ListNode(data)
            new_node.next=self.head    ##newnode的next链向self.head指向地址
            self.head=new_node   ## head指向刚进入的最前端节点

    def Insert(self,data):
        if self.head is None:
            self.head=ListNode(data)
            self.last_node=self.head
        else:
            new_node=ListNode(data)
            self.last_node.next=new_node
            self.last_node=new_node   ##用lastnode来记录当前最后一个节点，head始终是第一个节点

    def Delete(self,data):
        self.heads=self.head      ##heads类似于插入的lastnode用来操作链表，head需要始终指向表头，若用head来操作链表会造成head作为表头指向被删元素的前一个。
        if data != self.heads.data:    ##判断被删元素是否删表头元素
            while self.heads and self.heads.next.data != data:
                self.heads=self.heads.next
            if self.heads:
                self.heads.next=self.heads.next.next
            else:
                return False
        else: ##被删元素为表头时
            self.head=self.head.next

    def isNone(self):
        if self.head is None:
            return True
        else:
            return False

    def PrintList(self,node):
        if node is not None:
            print(node.data)
            self.PrintList(node.next)


class DoubleList(List):
    def PreInsert(self,data):
        if self.head is None:
            self.head=ListNode(data)
        else:
            new_node=DoubleListNode(data)
            new_node.next=self.head     
            self.head.rear=new_node
            self.head = new_node

    def Insert(self,data):   ##除了Insert和Delete需要重写，其他沿用父类即可
        if self.head is None:
           self.head=ListNode(data)
           self.last_node=self.head
        else:
           new_node=DoubleListNode(data)
           self.last_node.next=new_node   ##lastnode指向newnode
           new_node.rear=self.last_node  ##newnode的前指针rear指向lastnode
           self.last_node=new_node  ##newnode地址赋给lastnode，lastnode指向当前列表最后一个节


    def Delete(self,data):
        self.heads=self.head
        if self.heads.data == data: ##被删元素为表头时候
            self.head=self.head.next
            self.head.rear=None     ##若是头节点，则删除后rear指向None
        elif self.last_node.data == data:  ##被删元素为表尾时候
            self.last_node.rear.next=None
        else:
            while self.heads and self.heads.next.data != data:
                self.heads=self.heads.next
            if self.heads:
                self.heads.next=self.heads.next.next
                self.heads.next.rear=self.heads  ##先修改后指针next后改前指针rear
            else:
                return False








a=DoubleList()
for i in range(5):
    a.PreInsert(i)



a.PrintList(a.Get_Head())












