class Sort:

    def __init__(self):
        self.unsolvelist=[3,44,38,5,47,15,36,26,27,2,46,4,19,50]
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
        gap=int(len(list)/2)
        while gap >=1: ##总共循环次数
            for i in range(gap): ##gap等于分组数量，即被分开了gap个数组
                temp_list=[]
                for k in range(int(len(list)/gap)): ##gap个数组，总数为legnth，那么每个数组有length/gap个元素
                    temp_list.append(list[i+k*gap]) ##这里添加length/gap个元素,(i+k*gap,i+2k*gap)i为上层循环控制
                temp_list=sorted(temp_list)
                for j in range(len(temp_list)): ##对于排序好的temp_list数组，把值按照gap大小跨越赋值
                    list[i+j*gap]=temp_list[j]  ##i控制当前数组顺序，即第一个gap数组，第二个gap数组...etc
            gap=int(gap/2)

        print(self.unsolvelist)




    def Quick_sort(self,list,left,right):
        if left==right: ##在list为空时退出
            return
        cardinate_value=list[left] ##默认第一个数为基准数
        start_value=left  ##左边开始的哨兵索引
        last_value=right-1 ##右边开始的哨兵索引
        while True: ##参考onenote快排规则
            while last_value!=start_value and list[last_value] >= cardinate_value: ##先移动右边哨兵，当比基准数小时停下
                last_value=last_value-1
            while start_value!=last_value and list[start_value] <= cardinate_value: ##再移动左边哨兵，当比基准数大时停下
                start_value=start_value+1
            list[start_value],list[last_value]=list[last_value],list[start_value] ##哨兵对应的值交换
            if start_value==last_value: ##如果哨兵碰头了，则和基准数交换，第一轮完成后，基准数排序到正确的位置
                list[list.index(cardinate_value)],list[start_value]=list[start_value],list[list.index(cardinate_value)]
                break
        self.Quick_sort(list,left,start_value) ##对左边排序
        self.Quick_sort(list,start_value+1,right) ##对右边排序

        return list





    def Merge_sort(self,list):
        length=len(list)
        mid=int(length/2)
        if length == 1:  ##在只有单个元素时候退出递归
            return list
        ##下面开始拆分
        left=self.Merge_sort(list[:mid]) ##将之前合并的数组传入left数组
        right=self.Merge_sort(list[mid:])
        ##下面开始合并
        if left and right:
            temp=[] ##每一次都要清空temp数组的值
            length_l=int(len(left)) #介于数组可能分出[1,2] [3]这样一个长度为2一个长度为1，所以要分别找出两个length长度
            length_r=int(len(right))
            i,j=0,0
            while i < length_l and j<length_r:  ##详见onenote归并时候的规则
                min_value=min(left[i],right[j])
                if min_value == left[i]:
                    temp.append(min_value)
                    i=i+1
                    if i==length_l:   ##当其中一个数组空后，直接把另一边数组的所有元素加入temp数组
                        while j<length_r:
                            temp.append(right[j])
                            j=j+1

                elif min_value==right[j]: ##镜像同理
                    temp.append(min_value)
                    j=j+1
                    if j==length_r:
                        while i <length_l:
                            temp.append(left[i])
                            i=i+1

            return temp






a=Sort()
#print(sorted(a.unsolvelist))
#a.Bubble_sort(a.unsolvelist)
#a.Selection_sort(a.unsolvelist)
#a.Insertion_sort(a.unsolvelist)
#a.Shell_sort(a.unsolvelist)
#print(a.Merge_sort(a.unsolvelist))
#print(a.Quick_sort(a.unsolvelist,0,len(a.unsolvelist)))
#所有排序测试通过！


