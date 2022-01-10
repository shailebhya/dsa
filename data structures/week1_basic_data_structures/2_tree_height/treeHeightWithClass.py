 # python3

import sys
import threading


class Node:
    def __init__(self,name):
        self.key = name
        self.child = []

class TreeHeight:

    def __init__(self):
        self.n = int(input())
        self.input = [int(i) for i in input().split()]
        self.root = None
        self.nodes = []


    def read(self): #construct the tree
        nodes = []
        for i in range(self.n): 
            nodes.append(Node(i))
        j=0
        for i in self.input:    
            if i != -1:
                nodes[i].child.append(nodes[j])
            else:
                self.root = nodes[j]
            j += 1
        self.nodes = nodes

    def calculateHeight(self):
        rootNode = self.root
        def Height(rootNode):
            if rootNode is None:
                return 0
            if len(rootNode.child)==0:
                return 1
            else:
                h = []
                for i in range(len(rootNode.child)):
                    h.append(Height(rootNode.child[i]))

            return 1 + max(h)
        return Height(rootNode)


def main():
  tree = TreeHeight()
  tree.read()
  print(tree.calculateHeight())
    # compute_depth(n,parents)



# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
