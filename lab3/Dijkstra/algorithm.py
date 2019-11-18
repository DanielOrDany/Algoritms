from collections import namedtuple, deque
import unittest
import os

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

        while q: #V
            u = min(q, key=lambda vertex: dist[vertex])
            q.remove(u)

            if dist[u] == inf or u == dest:
                break

            for v, cost in neighbours[u]: #E
                if dist[u] + cost < dist[v]:  # Relax (u,v,a)
                    dist[v] = dist[u] + cost
                    previous[v] = u

        s, u = deque(), dest
        while previous[u]:
            s.appendleft(u)
            u = previous[u]
        s.appendleft(u)
        return s

class TestStringMethods(unittest.TestCase):

    def test_true(self):
        mArray = []

        data = open("data.txt","r")
        contents = data.readlines()
        for x in contents:
            res = [int(i) for i in x.split() if i.isdigit()]
            mArray.append(res)
        data.close()

        graph = Graph(mArray)

        self.assertEqual(graph.dijkstra(5, 100),  deque([5, 32, 27, 196, 118, 46, 178, 158, 150, 2, 47, 7, 100]))

    def test_file(self):
        assert os.path.exists("data.txt") == 1

if __name__ == '__main__':
    unittest.main()
