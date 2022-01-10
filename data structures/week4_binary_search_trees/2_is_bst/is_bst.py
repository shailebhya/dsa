#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def inOrder(itree,nodes):
  # print("i am in inOrder function")
  result = []
  id = 0
  stack = []
  tree = {"key":[0 for _ in range(nodes)],"left":[0 for _ in range(nodes)],"right":[0 for _ in range(nodes)]}
  # tree.key,tree.left,tree.right = itree[0],itree
  for i in range(nodes):
    tree["key"][i],tree["left"][i],tree["right"][i]=itree[i][0],itree[i][1],itree[i][2]
  # Finish the implementation
  # You may need to add a new recursive method to do that
  while True:
    if id !=-1:
      stack.append(id)
      id = tree['left'][id]
    elif stack:
      id = stack.pop()
      # yield tree.key[id]
      result.append(tree['key'][id])
      # tree.result.append(tree.key[stack.pop()])
      id = tree['right'][id]
    else:
      break

  return result


def IsBinarySearchTree(tree,nodes):
  if len(tree)==0:
    return True
  # Implement correct algorithm here
  ordered = inOrder(tree,nodes)
  # print(ordered)
  for i in range(1,len(ordered)):
    if ordered[i] < ordered[i-1]:
      # print(i)
      # print(ordered[i])
      # print(ordered[i-1])
      return False
  return True


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
    
  if IsBinarySearchTree(tree,nodes):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
