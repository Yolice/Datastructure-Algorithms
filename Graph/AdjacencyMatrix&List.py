from List import List
class AdjacencyListNode:
    def __init__(self,index,weight):
        self.index=index
        self.weight=weight
        self.next=None

class AdjList:
    def __init__(self):
        self.head=None


    def Get_head(self):
        return self.head


    def Insert(self,index,weight):
        if self.head is None:
            self.head=AdjacencyListNode(index,weight)
            self.last_node=self.head
        else:
            new_node=AdjacencyListNode(index,weight)
            self.last_node.next=new_node
            self.last_node=new_node



    def PrintList(self,node):
        if node is not None:
            print('['+str(node.index)+","+str(node.weight)+']',end=',')
            self.PrintList(node.next)



class Vertex: ##图中的顶点是抽象的，具体表示内容可以自己拓展
    def __init__(self,value):
        self.value=value



class Graph:   ##无向图
    def __init__(self):
        self.INFINITE = float("inf")  ##INFINITE大于python所有数




    def Receive_Graph_info(self):
        Vertexs=[]
        Edges=dict()
        print("输入你的顶点值,按e退出顶点值的输入")
        while True:
            vertex_value=input()
            if vertex_value == 'e':
                break
            Vertexs.append(vertex_value)
        print("输入你的图的边关系，按e退出")
        for vertex in Vertexs:
            print("输入"+str(vertex)+"顶点对应点边与权值，按e退出")
            while True:
                connect_edge=input(str(vertex)+"的对应边:")
                if connect_edge =='e':
                    break
                weight = input(str(vertex)+"与顶点"+str(connect_edge)+"对应的权值:")
                Edges[str(vertex)+"->"+str(connect_edge)]=weight

        return Vertexs,Edges



    def Generate_AdjacencyMatrix(self,Vertexs,Edges):  ##不维护用户输入的错误
        Vertexs_num=len(Vertexs)
        AdjacencyMatrix=[[ self.INFINITE for i in range(Vertexs_num)]for  i in range(Vertexs_num)]  ##利用列表生成式构造矩阵
        for i in range(Vertexs_num):
            AdjacencyMatrix[i][i]=0  ##每个顶点到自己到距离是0

        for edge_relationship in Edges:   ##利用边关系的数据，每次提取一组边关系，然后写入矩阵以及对应的权值
            temporylist=[]
            weight=Edges[edge_relationship]
            for i in edge_relationship.split('->'):
                temporylist.append(int(i))  ##split分割后是str格式，这里我需要int格式
            AdjacencyMatrix[temporylist[0]][temporylist[1]]=weight     ##如果利用无向图矩阵对称性质可以优化代码

        return AdjacencyMatrix




    def Generate_AdjacencyList(self,Vertexs,Edges):
        Vertexs_num=len(Vertexs)
        AdjacencyList=[]
        for vertex in Vertexs: ##每一次循环都把一个顶点作为head头加入领接表
            temporynode=AdjList()
            temporynode.Insert(vertex,0) ##初始化当前顶点，自己和自己的权值顶为0
            AdjacencyList.append(temporynode.Get_head())  ## 把控制链表的句柄head加入到领接表
            for key in Edges.keys():   ##把与当前顶点相关点边的顶点用insert方式插入结点
                vertex_relationship=key.split('->')
                start_value=int(vertex_relationship[0])  
                end_value=int(vertex_relationship[1])    ##split分割后默认是str格式，比较数值大小时候要用int转换
                if vertex == start_value: ##只处理和当前顶点有关的边
                    temporynode.Insert(Vertexs.index(end_value),Edges[key]) ##领接表用index索引指向与之关联的顶点
            temporynode=None

        return AdjacencyList



    def PrintAdjacencyList(self,AdjacencyList):
        for vertex in AdjacencyList:
            AdjList().PrintList(vertex)
            print()






'''
INF=float("inf")
matrix=[[INF for i in range(5)] for i in range(5)]
for i in range(5):
    matrix[i][i]=0

temporyvertexs=[0,1,2,3,4]
temporydict={'0->1':4,'0->2':4,'0->3':6,'0->4':6,'1->0':4,'1->2':2,'2->1':2,'2->0':4,'2->3':8,'3->2':8,'3->0':6,'3->4':9,'4->0':6,'4->3':9}
for edge_relationship in temporydict:
    a=[]
    w=temporydict[edge_relationship]
    for i in edge_relationship.split('->'):
        a.append(int(i))
    matrix[a[0]][a[1]]=w
print(matrix)
a=Graph()
v,w=a.Receive_Graph_info()
print(a.Generate_AdjacencyMatrix(v,w))
领接矩阵测试通过！
temporyvertexs=[0,1,2,3,4]
temporydict={'0->1':4,'0->2':4,'0->3':6,'0->4':6,'1->0':4,'1->2':2,'2->0':4,'2->1':2,'2->3':8,'3->0':6,'3->2':8,'3->4':9,'4->0':6,'4->3':9}

a=Graph()
a.PrintAdjacencyList(a.Generate_AdjacencyList(temporyvertexs,temporydict))
领接表测试通过！
'''
