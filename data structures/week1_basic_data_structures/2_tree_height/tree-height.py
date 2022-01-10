# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

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

    def compute_height(self):
            # Replace this code with a faster implementation
        maxHeight = 0
        for vertex in range(self.n):
            height = 0
            i = vertex
            while i != -1:
                height += 1
                i = self.parent[i]
            maxHeight = max(maxHeight, height)
        return maxHeight

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
  print(tree.compute_height())

threading.Thread(target=main).start()
