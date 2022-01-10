# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def more_optimal_sequence(n):
    allKeys = [0] * (n + 1)
    allMinOp = [0] + [0] * n

    for k in range(1, n + 1):
        currentKey = k - 1
        curr_min_ops = allMinOp[currentKey] + 1

        if k % 3 == 0:
            key = k // 3
            num_ops = allMinOp[key] + 1
            if num_ops < curr_min_ops:
                currentKey, curr_min_ops = key, num_ops

        if k % 2 == 0:
            key = k // 2
            num_ops = allMinOp[key] + 1
            if num_ops < curr_min_ops:
                currentKey, curr_min_ops = key, num_ops

        allKeys[k], allMinOp[k] = currentKey, curr_min_ops

    numbers = []
    k = n
    while k > 0:
        numbers.append(k)
        k = allKeys[k]

    return reversed(numbers)

input = sys.stdin.read()
n = int(input)
# sequence = list(optimal_sequence(n))
sequence = list(more_optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
