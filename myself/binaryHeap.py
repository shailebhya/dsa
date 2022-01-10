
class BinaryHeap:
    def __init__(self,size,maxSize,array):
        self.size = size 
        self.maxSize = maxSize
        self.array = array
    def __iter__(self):
        return self

class Node:
    def __init__(self,parent,leftChild,rightChild):
        self.parent = parent
        self.leftChild = leftChild
        self.rightChild = rightChild