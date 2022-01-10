# Uses python3
import sys

#Please use the divide and conquer algorithm
def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code 
    a.sort()
    m = a[len(a)//2]
    if a.count(m)>len(a)/2:
        return 1

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
