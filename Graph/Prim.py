import AdjacencyStore
import pprint

inf=float('inf')
#Vertexs=[0,1,2,3,4]
#Edges={'0->1':4,'0->2':4,'0->3':6,'0->4':6,'1->0':4,'1->2':2,'2->1':2,'2->0':4,'2->3':8,'3->2':8,'3->0':6,'3->4':9,'4->0':6,'4->3':9}

AdjacencyMatrix=AdjacencyStore.Graph().Generate_AdjacencyMatrix(Vertexs,Edges)
for i in range(len(AdjacencyMatrix[0])):
    AdjacencyMatrix[i][i]=inf


##pprint.pprint(AdjacencyMatrix)

class MinimumSpanningTree:
    def __init__(self):
        self.Visited=[]
        self.inf=float('inf')
        self.MinimumSpanningTree=[]



    def Prim(self,AdjacencyMatrix,Vertexs):
        Vertexs_size=len(Vertexs)
        self.Visited.append(Vertexs[0])
        i=0
        while i < Vertexs_size-1:  ##循环顶点数组-1次数
            minimum_weight=self.inf
            minimiun_weight_opposite_vertex=None
            minimum_weight_start_vertex=None
            vertex_relationship=None
            for vertex in self.Visited: ##找到Visited中的顶点所有边中权值最小的一条
                compare_list=AdjacencyMatrix[vertex]
                if min(compare_list) < minimum_weight:  ##如果有更小的权值，那么就记录下来
                    minimum_weight=min(compare_list) ##这里找到最小权值
                    minimiun_weight_opposite_vertex=Vertexs[compare_list.index(minimum_weight)] ##这是最小权值对应起始顶点对面的顶点
                    minimum_weight_start_vertex=vertex ##最小权值的起始顶点
                    vertex_relationship={'{}->{}'.format(minimum_weight_start_vertex,minimiun_weight_opposite_vertex):minimum_weight} ##这里筛选出了一条权值最小的边
            AdjacencyMatrix[minimum_weight_start_vertex][minimiun_weight_opposite_vertex] = AdjacencyMatrix[minimiun_weight_opposite_vertex][minimum_weight_start_vertex] = self.inf  ##把边选中后权值改为无限大防止下次再次被选中
            if minimiun_weight_opposite_vertex not in self.Visited: ##如果对应的顶点未被访问过，那么这条边是可以被选择的
                self.Visited.append(minimiun_weight_opposite_vertex) ##下次循环这个顶点也加入最小权值搜索过程
                self.MinimumSpanningTree.append(vertex_relationship) ##把上面找到最小权值边加入MST数组
            else: ##如果这个边被访问过了，那么这次循环重来
                i=i-1
            i=i+1
        return self.MinimumSpanningTree











print(MinimumSpanningTree().Prim(AdjacencyMatrix,Vertexs))




