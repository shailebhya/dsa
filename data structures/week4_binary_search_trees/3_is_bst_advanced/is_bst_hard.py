#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class Node:
    def __init__(self, a, b, c):
        self.key = a
        self.left = b
        self.right = c


def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  if len(tree)==0:
    return True
  stack = [(float('-inf'), tree[0], float('inf'))]
  while stack:
      min, root, max = stack.pop()
      if root.key < min or root.key >= max:
          return False
      if root.left != -1:
          stack.append((min, tree[root.left], root.key))
      if root.right != -1:
          stack.append((root.key, tree[root.right], max))
  return True


def main():
  n = int(sys.stdin.readline().strip())
  tree = [0 for _ in range(n)]
  # for i in range(n):
  #   tree.append(list(map(int, sys.stdin.readline().strip().split())))
  for i in range(n):
      a, b, c = map(int, input().split())
      node = Node(a, b, c)
      tree[i] = node
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
