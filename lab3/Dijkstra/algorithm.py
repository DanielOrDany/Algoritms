from collections import namedtuple, deque

inf = float('inf')
Edge = namedtuple('Edge', ['start', 'end', 'cost'])


class Graph():
    def __init__(self, edges):
        self.edges = [Edge(*edge) for edge in edges]
        self.vertices = {e.start for e in self.edges} | {e.end for e in self.edges}

    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Source don\'t exist in graph!'
        dist = {vertex: inf for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        dist[source] = 0
        q = self.vertices.copy()
        neighbours = {vertex: set() for vertex in self.vertices}
        for start, end, cost in self.edges:
            neighbours[start].add((end, cost))

        while q:
            u = min(q, key=lambda vertex: dist[vertex])
            q.remove(u)

            for v, cost in neighbours[u]:
                if dist[u] + cost < dist[v]:  # Relax (u,v,a)
                    dist[v] = dist[u] + cost
                    previous[v] = u

        s, u = deque(), dest
        while previous[u]:
            s.appendleft(u)
            u = previous[u]
        s.appendleft(u)
        return s

mArray = []
data = open("data.txt","r")
contents = data.readlines()
for x in contents:
    res = [int(i) for i in x.split() if i.isdigit()]
    mArray.append(res)
data.close()

graph = Graph(mArray)

print graph.dijkstra(5, 100)
