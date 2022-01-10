# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)-1
    # print("this is the number we searching for {}",x)
    # write your code here
    # print(len(a))
    while left<=right:
        m = (left+right)//2
        # print("this is left,right,left plus right",left,right,left+right)
        # if (left+right)//2>len(a)-1:
        #     return -1
        if a[m]==x:
            # print("here")
            return m
        elif a[m]<x:
            # print("hello")
            # print("x is greater")
            left=m+1
        elif a[m]>x:
            # print("x is lesses")
            right=m-1
    return -1



def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        # print(linear_search(a, x), end = ' ')
        print(binary_search(a, x), end = ' ')
