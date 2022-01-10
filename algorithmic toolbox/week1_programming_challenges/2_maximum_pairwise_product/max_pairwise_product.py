# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    print(n)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

x= [x for x in range(1,2*10**5+1)]
def max_pairwise_product_fast(numbers):
    n=len(numbers)

    index1 =0
    
    for i in range(0,n):
        if(numbers[i]>numbers[index1]):
            index1= i
    # print("Index 1: {}",index1)
    
    if index1==0:
        index2 = 1
    else:
        index2=0

    for j in range(0,n):
        if(j!=index1 and numbers[j]>numbers[index2]):
            index2=j
    # print("Index 2: {}",index2)
    
    return numbers[index1]*numbers[index2]



if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))