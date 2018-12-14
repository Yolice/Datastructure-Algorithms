from List import ListNode

class Stack():
    def __init__(self):
        self.top=None

    def Push(self,data):
        if self.top is None:
            self.top=ListNode(data)
        else:
            new_node=ListNode(data)
            new_node.next=self.top
            self.top=new_node

    def Get_Top(self):
        return self.top

    def IsNullStack(self):
        if self.top is None:
            return True
        else:
            return False

    def Pop(self):
        pop_value=self.top.data   ##先把要弹出的节点的值保存，再弹出栈顶
        self.top=self.top.next
        return pop_value

    def Traversal(self,top):
        if top:
            print(top.data)
            self.Traversal(top.next)


class Queue():
    def __init__(self):
        self.prev=None
        self.rear=None

    def Enqueue(self,data):
        if self.prev is None:
            self.prev=ListNode(data)
            self.rear=self.prev
        else:
            new_node=ListNode(data)
            self.rear.next=new_node
            self.rear=new_node


    def Dequeue(self):
        dequeue_value=self.prev.data
        self.prev=self.prev.next
        return dequeue_value


    def IsNullQueue(self):
        if self.prev is None:   ##这里不判断rear是否None是因为rear还指向了最后一个节点，但在稍后会回收这个节点
            return True
        else:
            return False

    def Traversal(self,prev):
        if prev:
            print(prev.data)
            self.Traversal(prev.next)

    def Get_prev(self):
        return self.prev

    def Get_rear(self):
        return self.rear




'''
a=Queue()

for i in range(10):
    a.Enqueue(i)

for i in range(10):
    a.Dequeue()

print(a.IsNullQueue())
'''




