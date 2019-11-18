from collections import *


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, v, e):
        self.graph[e].append(v)

    def bfs(self, root):
        result = [root]
        visited, queue = set(), deque([root])
        visited.add(root)
        while queue:
            vertex = queue.popleft()
            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
                    result.append(neighbour)

        return result


g = Graph()

documents = {}

data = open("govern.in", "r")
contents = data.readlines()

number = 0
for document in contents:
    res = [i for i in document.split()]
    if res[0] not in documents.keys():
        documents.update({res[0]: number})
        number = number + 1

for document in contents:
    res = [i for i in document.split()]
    if res[1] not in documents.keys():
        documents.update({res[1]: number})
        number = number + 1


print "\n\nConvert documents to numbers: \n"

for document in contents:
    res = [i for i in document.split()]
    print str(documents[res[0]]) + ": " + str(res[0]) + " | " + str(documents[res[1]]) + ": " + str(res[1])
    g.addEdge(documents[res[1]], documents[res[0]])

for g_ed in g.bfs(0)[::-1]:
    for ver, ed in documents.items():
        if ed == g_ed:
            print ver

data.close()