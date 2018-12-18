import AdjacencyStore
import pprint
import queue

class Graph_Traversal:
    def __init__(self,Vertexs,Edges):
        self.CheckVertexs=[]  ##初始化为空list，如果访问过了就把顶点index加入这个数组，如果查找时候发现存在就代表已经访问过了
        self.Vertexs=Vertexs
        self.Edges=Edges





    def FindNeiborhoodNode(self,vertex,AdjacencyMatrix):
        NeigborhoodNodes = []
        index = 0
        for v in AdjacencyMatrix[vertex]:  ##找出每个顶点的相连顶点
            if v == 1:
                NeigborhoodNodes.append(self.Vertexs[index])  ##例子中索引值即为顶点值
            index = index + 1
        return NeigborhoodNodes





    def DepthFirstSearch(self,vertex,AdjacencyMatrix):
        NeiborhoodNodes=self.FindNeiborhoodNode(vertex,AdjacencyMatrix)
        print(vertex)  ##这里只是打出顶点的值，具体可以左别的操作
        self.CheckVertexs.append(vertex)
        for node in NeiborhoodNodes:
            if node in self.CheckVertexs:
                continue
            else:
                self.DepthFirstSearch(node,AdjacencyMatrix)
        self.CheckVertexs=[]





    def BreadthFirstSearch(self,vertex,AdjacencyMatrix):
        Vertexs_Queue=queue.Queue() ##BFS用队列，DFS用栈或者递归
        Vertexs_Queue.put(vertex) ##先入队一个顶点
        while Vertexs_Queue.empty() is False: ##当队列不空时候
            operate_vertex=Vertexs_Queue.get()
            NeiborhoodNodes=self.FindNeiborhoodNode(operate_vertex,AdjacencyMatrix) ##直接出队，取得该顶点当相关顶点
            for node in NeiborhoodNodes:
                if node in self.CheckVertexs:  ##如果已经该相关顶点已经被访问过了，那么直接无视continue，关注下一个相关顶点
                    continue
                else:
                    Vertexs_Queue.put(node) ##当一个顶点退出时候把他相关的未被访问过的顶点入队
            print(operate_vertex) ##可以别的抽象的对顶点的操作
            self.CheckVertexs.append(operate_vertex) ##出队后标记为访问过了
        self.CheckVertexs=[]  ##退出时候清空下列表内容
















'''
Vertexs=[0,1,2,3,4,5,6,7]
Edges={'0->1':1,'1->3':1,'2->1':1,'3->2':1,'3->4':1,'4->5':1,'5->7':1,'6->4':1,'7->6':1} ##没有权值的有向图默认给一个1的权值表示两个顶点是相互链接的

Example=AdjacencyStore.Graph()
AdjacencyMatrix=Example.Generate_AdjacencyMatrix(Vertexs,Edges)
a=Graph_Traversal(Vertexs,Edges)
a.DepthFirstSearch(Vertexs[0],AdjacencyMatrix) ##从0开始，图任意点都可以是起点
a.BreadthFirstSearch(Vertexs[0],AdjacencyMatrix)
pprint.pprint(AdjacencyMatrix)
BFS和DFS样本全部测试通过！
'''


