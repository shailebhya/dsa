# Uses python3
import sys


#Stupid idiot you forgot to delete the other elemtn indexes
def get_optimal_value(n,capacity, weights, values):
    value = 0.
    totalWeight=0.
    # write your code here
    if n==1 and capacity<=weights[0]:
        return values[0]*capacity/weights[0]
    elif capacity>=weights[0] and n==1:
        return values[0]

    vpwList =[]
    for i in range(len(weights)):
        vpwList.append(values[i]/weights[i])

    while totalWeight<=capacity:
        x= vpwList.index(max(vpwList))
        if capacity==0:
            return 0
        elif weights[x]+totalWeight>capacity:
            value=value+values[x]*(capacity-totalWeight)/weights[x]
            return value
        else:
            value=value+values[x]
            totalWeight=totalWeight+weights[x]
            del vpwList[x]
            del weights[x]
            del values[x]

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(n,capacity, weights, values)
    print("{:.10f}".format(opt_value))
