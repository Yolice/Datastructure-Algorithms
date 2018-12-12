class Heap:  ##大顶堆
    def __init__(self):
        self.HeapArray=['defalut']


    def swap(self,list,index_a,index_b):
        list[index_b],list[index_a]=list[index_a],list[index_b]


    def ShiftUp(self,Array,index):
        while index != 1:
            ParentIndex=int(index/2)
            if Array[index] > Array[ParentIndex]:
                self.swap(Array,index,ParentIndex)
            index=int(index/2)


    def Get_Array(self):
        return self.HeapArray


    def IsTop(self):
        try:
            if self.HeapArray[1]:
                return True
        except:
            return False


    def Get_Top(self):
        if self.IsTop():
            return self.HeapArray[1]


    def Get_Array_Size(self,Array):
        count=0
        for i in Array:
            count=count+1
        return count ##堆数组第零个是哨兵"default"，真正的堆元素从第一个数起


    def PopTopElement(self,Array):
        if self.IsTop():
            LastElementIndex=self.Get_Array_Size(Array)-1  ##堆数组第零个是哨兵"default"，真正的堆元素从第一个数起
            self.swap(Array,1,LastElementIndex)
            pop_value=Array.pop()  ##把第一个值弹出/删除
            LastElementIndex=LastElementIndex-1 ##弹出后最后一个值index-1
            self.ShiftDown(Array,1,LastElementIndex/2)  ##LastElementIndex/2指向最后一个非叶节点,在pop元素中，和最后一个元素交换后从第一个值下沉
            return pop_value
        else:
            print("空堆无堆顶元素")




    def Push(self,Array,data): ##从零构造一个二叉堆时候每次插入新值到末尾时都堆末尾堆值做一次上浮
        Array.append(data)
        self.ShiftUp(Array,self.Get_Array_Size(Array)-1)



    def CreateHeap(self,data):
        self.Push(self.HeapArray,data)




    def ShiftDown(self,Array,index,limit):  ##limit代表最后一个非叶节点的index索引值(最后一个值index/2)，如果超出这个非叶节点则不用继续下沉
        Length=limit*2
        while index <= int(limit):  ##非叶节点才有交换意义
            if index*2+1 < Length: ##加入左右子节点都存在
                if Array[index*2]>Array[index*2+1] and Array[index*2]>Array[index]: ##左大于右,大顶堆谁大换谁
                    self.swap(Array,index,index*2)
                    index=index*2
                elif Array[index*2+1]>Array[index*2] and Array[index*2+1]>Array[index]:
                    self.swap(Array,index,index*2+1)
                    index=index*2+1
            else:  ##非则只存在一个左节点，这是又二叉堆特性决定的，它不会出现只有右子节点的情况
                if Array[index*2]>Array[index]:
                    self.swap(Array,index,index*2)
                    index=index*2













a=Heap()
a.CreateHeap(5)
a.CreateHeap(9)
a.CreateHeap(3)
a.CreateHeap(7)
a.CreateHeap(6)
a.CreateHeap(5)

print(a.Get_Array())
