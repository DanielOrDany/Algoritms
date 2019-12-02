import unittest
import filecmp
import os
from collections import defaultdict


def write_result(root, file_in, file_out):
    graph = Graph()

    input_data = open(file_in, "r")
    contents = input_data.readlines()

    for word in contents:
        if len(root) >= len(word.rstrip()):
            graph.input_words.append(word.rstrip())

    sorted_list = sorted(graph.input_words, key=len, reverse=True)

    graph.input_words = sorted_list
    graph.find_max_words(root)

    result_file = open(file_out, "w+")
    list = graph.bfs(0)

    result = []
    for r in list:
        result.append(graph.input_words[r])

    if len(result) == 1:
        print "max: " + str(len(result)) + " > " + str(remove_unnecessary_nodes(result))
    elif len(result) > 1:
        print "max: " + str(len(result) - 1) + " > " + str(remove_unnecessary_nodes(result))
    for word in result:
        result_file.write(word + "\n")

    result_file.close()
    input_data.close()


def sub_word(word, v):
    sw = word[:v] + word[v + 1:]
    return sw


def remove_unnecessary_nodes(list):
    previous_length = 0
    for x in list:
        if len(x) == previous_length:
            list.remove(x)
        previous_length = len(x)

    return list


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.found_words = []
        self.input_words = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def add_word(self, v):
        self.found_words.append(v)

    def find_max_words(self, start_word):

        for v in range(len(start_word)):
            generated_word = sub_word(start_word, v)

            if generated_word in self.input_words:
                self.add_word(generated_word)
                self.find_max_words(generated_word)
                u = self.input_words.index(generated_word)
                v = self.input_words.index(start_word)
                #print "u " + str(u) + " " + generated_word + ", v " + str(v) + " " + start_word
                self.add_edge(v, u)

            elif start_word in self.input_words:
                if start_word not in self.found_words:
                    self.add_word(start_word)
                    self.find_max_words(start_word)
                    u = self.input_words.index(start_word)
                    v = self.input_words.index(start_word)
                    #print "u " + str(u) + " " + start_word + ", v " + str(v) + " " + start_word
                    self.add_edge(v, u)

    def bfs(self, s):
        visited = [False] * (max(self.graph) + 2)

        queue = []
        result = []

        queue.append(s)
        visited[s] = True

        while queue:

            s = queue.pop(0)
            result.append(s)

            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

        return result


class Test(unittest.TestCase):
    def test_file_exist_one(self):
        self.assertEqual(os.path.exists('./example_one.out'), True)

    def test_right_answer_one(self):
        self.assertEqual(filecmp.cmp('example_one.out', 'right_one.out'), True)

    def test_file_exist_two(self):
        self.assertEqual(os.path.exists('./example_two.out'), True)

    def test_right_answer_two(self):
        self.assertEqual(filecmp.cmp('example_two.out', 'right_two.out'), True)

    def test_file_exist_three(self):
        self.assertEqual(os.path.exists('./example_three.out'), True)

    def test_right_answer_three(self):
        self.assertEqual(filecmp.cmp('example_three.out', 'right_three.out'), True)


if __name__ == '__main__':
    # First test
    write_result("crates", "example_one.in", "example_one.out")

    # Second test
    write_result("bcad", "example_two.in", "example_two.out")

    # Last test
    write_result("yetanotherword", "example_three.in", "example_three.out")

    unittest.main()
