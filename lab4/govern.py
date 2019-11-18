import unittest
import filecmp
import os
from collections import defaultdict


class Graph:
    def __init__(self):
        self.edges = defaultdict(list)
        self.docs = []
        self.root = 0

    def add_edge(self, v, e):
        self.edges[v].append(e)
        self.edges[e] = self.edges[e]
        if v not in self.docs:
            self.docs.append(v)
        if e not in self.docs:
            self.docs.append(e)

    def visit_document(self, v, visited, sort_list):
        visited[v] = True
        for neighbour in self.edges[v]:
            if not visited[neighbour]:
                self.visit_document(neighbour, visited, sort_list)

        sort_list.append(v)

    def find_order(self):
        if self.is_cyclic():
            return "graph has a cycle"

        received_documents = {document: False for document in self.edges}
        sort_list = []

        for v in self.edges:
            if not received_documents[v]:
                self.visit_document(v, received_documents, sort_list)

        return sort_list

    def is_cyclic(self):
        visited = [False] * len(self.docs)
        rec_stack = [False] * len(self.docs)

        for node in self.docs:
            if not visited[self.docs.index(node)]:
                if self.is_cyclic_util(node, visited, rec_stack):
                    return True

        return False

    def is_cyclic_util(self, v, visited, rec_stack):
        visited[self.docs.index(v)] = True
        rec_stack[self.docs.index(v)] = True

        for neighbour in self.edges[v]:
            if not visited[self.docs.index(neighbour)]:
                if self.is_cyclic_util(neighbour, visited, rec_stack):
                    return True

        return False


class TestStringMethods(unittest.TestCase):

    def test_file_ex(self):
        self.assertEqual(os.path.exists('./govern.out'), True)

    def test_file_ex(self):
        self.assertEqual(filecmp.cmp('govern.out', 'right.out'), True)

if __name__ == '__main__':
    g = Graph()
    data = open("govern.in", "r")
    contents = data.readlines()

    for document in contents:
        res = [i for i in document.split()]
        g.add_edge(res[0], res[1])

    f = open("govern.out", "w+")
    for item in g.find_order():
        f.write(item + "\n")
    f.close()

    unittest.main()

