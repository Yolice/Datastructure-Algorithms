class Sort:

    def __init__(self):
        self.unsolvelist=[3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
        self.minvalue=None


    def Bubble_sort(self,list):
        length=len(list)
        for i in range(length-1):
            for j in range(length-i-1):
                if list[j]>list[j+1]:
                    list[j],list[j+1]=list[j+1],list[j]  ##python中类似c语言的swap函数不起作用

        print(self.unsolvelist)



    def HeapSort(self):
        pass ##参考BinaryHeap



    def Selection_sort(self,list):   ##选择排序默认第一个值为最小值，之后对后面数比较，如果出现更小的则把那个数选择为最小的数，第一轮结束后
                                     ##与第一个数交换，就选出了第一个最小的数，以此类推。
        length=len(list)
        for i in range(length-1):
            minvalue=i  ##minvalue是代表index索引值
            for j in range(length-i-1):
                if list[minvalue]>list[i+j+1]:
                    minvalue=i+j+1
            list[i],list[minvalue]=list[minvalue],list[i]


        print(self.unsolvelist)




    def Insertion_sort(self,list): ##插入排序每次都从元数组挑一个数插入到已经被排序到数组里，然后从后面往前排序
        Sorted_list=[]
        length=len(list)
        for i in range(length): ##这里对整个数组元素操作，所以循环整个length（元素个数）长度
            if len(Sorted_list) == 0:  ##第一次直接把值加入被排序的数组
                Sorted_list.append(list[0])
            else:
                Sorted_list.append(list[i]) ##第二次开始，每次都插入一个原数组的数
                for j in range(i): ##i为当前调整有序数组的次数
                    if Sorted_list[i-j]<Sorted_list[i-j-1]: ##从后往前排，如果乱序就调整，如果顺序正常则无视进入下个循环。i-j可以从
                                                            ##最后一个元素定位,i-j-1就是倒数第二个元素
                        Sorted_list[i-j],Sorted_list[i-j-1]=Sorted_list[i-j-1],Sorted_list[i-j]

        self.unsolvelist=Sorted_list
        print(Sorted_list)








    def Shell_sort(self,list):
        pass





a=Sort()
#print(sorted(a.unsolvelist))
#a.Bubble_sort(a.unsolvelist)
#a.Selection_sort(a.unsolvelist)
#a.Insertion_sort(a.unsolvelist)


