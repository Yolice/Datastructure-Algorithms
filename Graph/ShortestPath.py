import pprint
import AdjacencyStore
#Vertexs=[0,1,2,3,4]
#Edges={'0->1':2,'0->2':6,'0->3':7,'1->3':3,'1->4':6,'2->4':1,'3->4':5}
Vertexs=[1,2,3,4,5,6]
Edges={'1->2':1,'1->3':12,'2->3':9,'2->4':3,'3->5':5,'4->3':4,'4->5':13,'4->6':15,'5->6':4}

Matrix=AdjacencyStore.Graph().Generate_AdjacencyMatrix(Vertexs,Edges)
INF=float("inf")


class ShortestPath:
    def __init__(self):
        self.confirm_vertex=[]



    def Floyd(self,AdjacencyMatrix,Vertexs_Length):
        for i in range(Vertexs_Length):
            for j in range(Vertexs_Length):
                for k in range(Vertexs_Length):
                    if AdjacencyMatrix[i][j] > AdjacencyMatrix[i][k]+AdjacencyMatrix[k][j]:
                        AdjacencyMatrix[i][j]=AdjacencyMatrix[i][k]+AdjacencyMatrix[k][j]

        return AdjacencyMatrix



    def Find_Min(self,list,confirm_vertex):
        min=INF
        for i in list:
            if min>i and i!=0 and i not in confirm_vertex:
                min,i=i,min

        return min




    def Dijkstra(self,AdjacencyMatrix,Vertexs,index): ##index代表想要找哪个顶点最短路径的在矩阵中索引值
        distance=AdjacencyMatrix[index] ##哪个当作源点，就取哪一行
        self.confirm_vertex.append(distance[index]) ##默认初始顶点
        for i in range(len(distance)-2): ##n个点，只需要操作n-2次就行了
            temp=[]
            minimum_cost_weight=self.Find_Min(distance,self.confirm_vertex) ##找出当前代价最小的一条边
            minimum_cost_vertex=distance.index(minimum_cost_weight) ##代价最小一条边对应的顶点
            for k in AdjacencyMatrix[minimum_cost_vertex]:
                if k!=INF and k!= 0:
                    temp.append(AdjacencyMatrix[minimum_cost_vertex].index(k)) ##代价最小边对应顶点的边的关系
            for j in temp: ##依次比较，如果在通过代价最小边对应顶点比直接去耗费代价小，那么更新对应的值(具体解释看onenote笔记最短源路径)
                if distance[j] > distance[minimum_cost_vertex]+AdjacencyMatrix[minimum_cost_vertex][j]:
                    distance[j]=distance[minimum_cost_vertex]+AdjacencyMatrix[minimum_cost_vertex][j]
            self.confirm_vertex.append(distance[minimum_cost_vertex]) ##把已经找到点对应的权值加入数组，以后选最小权值跳过这个数组的值


        return distance








'''
[[0, 1, 12, inf, inf, inf],
 [inf, 0, 9, 3, inf, inf],
 [inf, inf, 0, inf, 5, inf],
 [inf, inf, 4, 0, 13, 15],
 [inf, inf, inf, inf, 0, 4],
 [inf, inf, inf, inf, inf, 0]]
'''






print(ShortestPath().Dijkstra(Matrix,Vertexs,0)) ##找出顶点0的最短路径信息
pprint.pprint(Matrix)

