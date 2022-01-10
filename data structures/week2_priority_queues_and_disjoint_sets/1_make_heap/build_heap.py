# python3
# q - using min heap(root is minimum) property to convert array into heap
# input - int = 5
#output  = no. of swaps and followed by indices of swap | for eg . 2
#                                                                  1 3
#                                                                  4 2
#                                                                  3 2
# Study the question correctly you idiot 
def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps

def build_heap_properly(arr,n):
    # For a min heap (root is minimum)
    swaps =[]
    def leftChild(i):
        return 2*i+1 #0 based indexing
    def rightChild(i):
        return 2*i+2 # 0 based indexing
    def parent(i):
        return (n-1)//2
    # This is the sift down function    
    def siftDown(i):
        maxIndex = i
        l  = leftChild(i)
        if l<n and arr[l]<arr[maxIndex]:
            maxIndex = l
        r = rightChild(i)
        if r<n and arr[r]<arr[maxIndex]:
            maxIndex = r
        if i != maxIndex:
            # print("swappin")
            arr[i],arr[maxIndex]=arr[maxIndex],arr[i]
            swaps.append((i,maxIndex))
            siftDown(maxIndex)

    for i in range(n//2,-1,-1):
        # print("the i in for loop is currently",i)
        siftDown(i)
    # print(arr)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    # swaps = build_heap(data)
    swaps  = build_heap_properly(data,len(data))

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
