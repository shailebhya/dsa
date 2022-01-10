# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    w = [0] + w
    totalItems = len(w)
    capacity = W + 1

    # Create a weight matrix and write in initial values.
    tWeights = [[0 for _ in range(totalItems)] for _ in range(capacity)]

    for i in range(1, totalItems):
        for j in range(1, capacity):
            tWeights[j][i] = tWeights[j][i - 1]
            if w[i] <= j:
                val = tWeights[j - w[i]][i - 1] + w[i]
                if tWeights[j][i] < val:
                    tWeights[j][i] = val

    return tWeights[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
