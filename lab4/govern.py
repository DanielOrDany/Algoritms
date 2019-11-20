import unittest
import filecmp
import os
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic_util(self, v, visited, rec_stack):
        visited[v] = True
        rec_stack[v] = True

        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.is_cyclic_util(neighbour, visited, rec_stack) == True:
                    return True
            elif rec_stack[neighbour] == True:
                return True

        rec_stack[v] = False
        return False

    def is_cyclic(self):
        visited = [False] * (len(self.graph) + 1)
        rec_stack = [False] * (len(self.graph) + 1)

        for node in range(len(self.graph) + 1):
            if visited[node] == False:
                if self.is_cyclic_util(node, visited, rec_stack) == True:
                    return True
        return False

    def dfs(self, v, visited, stack):
        visited[v] = True

        for i in self.graph[v]: #search in neighbours
            if visited[i] == False:
                self.dfs(i, visited, stack)

        stack.insert(0, v)

    def sort_documents(self):
        if self.is_cyclic():
            return "graph has a cycle"

        visited = [False] * (len(self.graph) + 1)   #7/8, +1
        stack = []

        for i in range(len(self.graph) + 1):
            if visited[i] == False:
                self.dfs(i, visited, stack)

        return stack


class TestStringMethods(unittest.TestCase):
    def test_file_exist(self):
        self.assertEqual(os.path.exists('./govern.out'), True)

    def test_right_answer(self):
        self.assertEqual(filecmp.cmp('govern.out', 'right.out'), True)


if __name__ == '__main__':
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

    for document in contents:
        res = [i for i in document.split()]
        print str(documents[res[0]]) + ": " + str(res[0]) + " | " + str(documents[res[1]]) + ": " + str(res[1])
        g.add_edge(documents[res[1]], documents[res[0]])

    f = open("govern.out", "w+")

    for g_ed in g.sort_documents():
        for v, ed in documents.items():
            if ed == g_ed:
                f.write(v + "\n") #\n after last item, done!

    f.close()
    data.close()

    unittest.main()
