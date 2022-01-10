# Uses python3
import sys
import random

def partition3( a,  l,  r):

    y = l  
    i = l  
    z = r
    pivot = a[l]  
                   
    while i <= z:      
        if a[i] < pivot:
            a[y], a[i] = a[i], a[y]
            y += 1
            i += 1
        elif a[i] > pivot:
            a[i], a[z] = a[z], a[i]
            z -= 1
        else:
            i += 1
            
    return y, z




def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    # m=
    y,z=partition3(a,l,r)
    randomized_quick_sort(a,l,y-1)
    randomized_quick_sort(a,z+1, r)
    # randomized_quick_sort(a, l, m - 1)
    # randomized_quick_sort(a, m + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
