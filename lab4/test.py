from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFS(self,v,vertex):
        visited = [False]*vertex
        print(self. graph)
        # print(len(self.graph),"+++")
        self.DFSUtil(v,visited)

    def DFSUtil(self,v,visited):
        visited[v]=True
        print(v)

        for i in self.graph[v]:
            if visited[i] == False:
                # print(visited)
                self.DFSUtil(i,visited)
g= Graph()

vertex=8

g.addEdge(0,5)
g.addEdge(0,2)
g.addEdge(0,1)
g.addEdge(1,4)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,7)
g.addEdge(5,4)
g.addEdge(5,6)
g.addEdge(6,4)

g.DFS(0,vertex)