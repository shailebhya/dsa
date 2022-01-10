#Uses python3

import sys


def explore(adj,x,visited):
    visited[x]=1
    for i in range(len(adj[x])):
        if (not visited[adj[x][i]]):
            if(explore(adj, adj[x][i],visited)):
                return 1
    return 0 

def reach(adj):
    #write your code here
    # print(adj,x,y)
    # [[1, 3], [0, 2], [1, 3], [2, 0]] 0 3
    visited = [0] * len(adj)


    return explore(adj,visited)

def acyclic(adj):
    print(adj)
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
