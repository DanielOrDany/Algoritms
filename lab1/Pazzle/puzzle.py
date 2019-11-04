from time import time
import random


q_comparisons = 0
q_swaps = 0

class Puzzle:
    def __init__(self, height, width, elements, about):
        self.height = height
        self.width = width
        self.elements = elements
        self.about = about

    def __repr__(self): return "\n height: " + str(self.height) + "  width: " + str(self.width) + "  elements: " + str(self.elements) + "  about: " + self.about + "\n"

def bubbleSort (array):
    comparisons = 0
    swaps = 0
    start = time()
    if not array:
        return []
    else:
        for i in range(0, len(array)): #first w b 0
            for j in range(0, len(array) - i - 1): # 0 -> 6 - 0 -> -1 -> 0 -> 5]
                comparisons += 1
                if array[j].elements < array[j + 1].elements: # 5 + 1 = 6
                    swaps += 1
                    (array[j], array[j + 1]) = (array[j + 1], array[j]) # 5 -><- 6
    end = time()
    compilation_time = end - start
    print("\nbubbleSort")
    print("compilation time: %.20f" % compilation_time)
    print("comparisons: " + str(comparisons) + "\nswaps: " + str(swaps))
    return "result:\n" + str(array)

def quickSort(array):
    if not array:
        return []
    else:
        pivots = []
        lesser = []
        greater = []
        for x in array:
            global q_comparisons
            global q_swaps
            q_comparisons += 1
            if x.height == array[0].height: # zero | else..
                #global q_comparisons
                q_comparisons += 1
                pivots.append(x)
                q_swaps += 1
            elif x.height < array[0].height:
                #global q_comparisons
                q_comparisons += 1
                lesser.append(x)
                #global q_swaps
                q_swaps += 1
            else:
                #global q_comparisons
                q_comparisons += 1
                greater.append(x)
                #global q_swaps
                q_swaps += 1
            lesser = quickSort(lesser)
            greater = quickSort(greater)
    return lesser + pivots + greater

p6 = Puzzle(60,75,350,"puzlik_6")
p5 = Puzzle(50,65,300,"puzlik_5")
p4 = Puzzle(40,55,250,"puzlik_4")
p3 = Puzzle(30,45,200,"puzlik_3")
p2 = Puzzle(20,35,150,"puzlik_2")
p1 = Puzzle(10,25,100,"puzlik_1")
puzzle_array = [p6, p2, p3, p4, p5, p1]

print(bubbleSort(puzzle_array))

print("\nQuick sort")
start = time()
print(quickSort(puzzle_array))
end = time()
compilation_time = end - start
print("compilation time: %.20f" % compilation_time )
print("comparisons: " + str(q_comparisons) + "\nswaps: " + str(q_swaps))
