# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size



# preorder , inorder  ,postorder = 1,2,3 th time we visit the particuar object while traversing the treee
class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    # print("i am in inOrder function")
    self.result = []
    id = 0
    stack = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    while True:
      if id !=-1:
        stack.append(id)
        id = self.left[id]
      elif stack:
        id = stack.pop()
        # yield self.key[id]
        self.result.append(self.key[id])
        # self.result.append(self.key[stack.pop()])
        id = self.right[id]
      else:
        break

    return self.result

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    id = 0
    stack = []
    while True:
      if id !=-1:
        self.result.append(self.key[id])
        stack.append(id)
        id = self.left[id]
      elif stack:
        id = stack.pop()
        id = self.right[id]
      else:
        break    
    return self.result

  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    stack=[0]
    while stack:
      id = stack.pop()
      self.result.append(self.key[id])
      left_id = self.left[id]
      right_id = self.right[id]
      if left_id != -1:
          stack.append(left_id)
      if right_id != -1:
          stack.append(right_id) 
    self.result.reverse()
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
