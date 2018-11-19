class ListNode():
    def __init__(self,data):
        self.data=data
        self.next=None


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
        self.heads=self.head      ##heads用来操作链表，head需要始终指向表头，若用来操作链表会造成head作为表头指向被删元素的前一个。
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


