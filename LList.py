class LNode:
    def __init__(self,elem,next=None):
        self.elem=elem
        self.next=next

class LList:   ##每个LList的实例都是一个链表
    def __init__(self):
        self.head=None     ##每个空链表默认有个head节点

    def is_empty(self):
        if self.head is None:
            return True

    def pop(self):
        e=self.head.elem
        self.head=self.head.next    ##从表头逐个删除，并返回值e
        return e

    def append(self,elem):
        if self.head is None:
            self.head=LNode(elem)
            return
        p=self.head
        while p.next is not None:
            p=p.next   ##操作完毕后找到最后一个元素
        p.next=LNode(elem)

    def pop_last(self):
        p=self.head
        if p.next is None:
            e=p.elem
            self.head=None
            return e
        while p.next.next is not None:
            p=p.next
        e=p.elem
        p.next=None
        return e

    def printall(self):
         p=self.head
         while p is not None:
             print(p.elem, end=' ')
             if p.next is not None:
                 print(", ",end=' ')
             p=p.next
         print(" ")

    def filter(self,func):  ##func指某种特定的操作函数
        p=self.head
        while p is not None:
            if func(p.elem):
                yield p.elem  ##生成器
            p=p.next

    def reverses(self):
        p=None
        while self.head is not None:
            q=self.head
            self.head=q.next
            q.next=p
            p=q
        self.head=p

class LList_advance(LList):  ##新添加了rear指向最后一个节点
    def __init__(self):
        LList.__init__(self)
        self.rear=None    ##rear直接指向链表的尾节点

    def append(self,elem):
        if self.head is None :
            self.head=LNode(elem)
            self.rear=self.head
        else :
            self.rear.next=LNode(elem)
            self.rear=self.rear.next

    def pop_last(self):
        p=self.head
        if p.next is None:
            e=p.elem
            self.head=None
            return e
        while p.next.next is not None:  ##定位到倒数第二个节点
            p=p.next
        e=p.elem
        p.next=None  ##最后一个节点删除
        self.rear=p  ##倒数第二个节点变成最后一个节点，由rear指向
        return e

class DoubleLNode(LNode):
    def __init__(self,elem,prev=None,next=None):
        LNode.__init__(self,elem,next)
        self.prev=prev

class DoubleList(LList_advance):
    def __init__(self):
        LList_advance.__init__(self)

    def append(self,elem):
        p=DoubleLNode(elem,self.rear,None)   ##新创建的p节点有self.rear的信息，即有链表最后一个节点的信息
        if self.head is None:
            self.head=p
        else:
            p.prev.next=p     ##最后一个节点的next链向新创建的p节点
        self.rear=p  ##把p的地址赋给self.rear，这样self.rear指向最后一个节点

    def pop(self):
        e=self.head.elem
        self.head=self.head.next
        if self.head is not None:  ##删除head时，prev还链向之前的节点，所以要赋值None
            self.head.prev=None
        return e

    def pop_last(self):
        e=self.rear.elem
        self.rear=self.rear.prev
        if self.rear is None:   ##如果之前的操作是对最后一个节点操作，那么rear.prev=None 所以rear为None
            self.head=None
        else:
            self.rear.next=None  ##最后一个节点地址赋给rear后把最后一个地址变成None然后又Python回收
        return e


'''
mlist=LList()
for i in range(10):
    mlist.append(i)
mlist.printall()
'''


'''
mlist1=LList_advance()
for i in range(20):
    mlist1.append(i)
mlist1.printall()
'''

