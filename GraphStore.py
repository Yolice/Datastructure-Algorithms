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



    def Generate_AdjacencyMatrix(self,Vertexs,Edgess):  ##不对超出矩阵范围错误作捕捉
        Vertexs_num=len(Vertexs)
        AdjacencyMatrix=[[ self.INFINITE for i in range(Vertexs_num)]for  i in range(Vertexs_num)]  ##利用列表生成式构造矩阵
        for i in range(Vertexs_num):
            AdjacencyMatrix[i][i]=0  ##每个顶点到自己到距离是0

        for edge_relationship in Edgess:   ##利用边关系的数据，每次提取一组边关系，然后写入矩阵以及对应的权值
            temporylist=[]
            weight=Edgess[edge_relationship]
            for i in edge_relationship.split('->'):
                temporylist.append(int(i))  ##split分割后是str格式，这里我需要int格式
            AdjacencyMatrix[temporylist[0]][temporylist[1]]=weight     ##如果利用无向图矩阵对称性质可以优化代码

        return AdjacencyMatrix



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
'''
a=Graph()
v,w=a.Receive_Graph_info()
print(a.Generate_AdjacencyMatrix(v,w))

