# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_fast(n):
    # nList=[i for i in range(n)]
    fibList = [0,1]
    # print("Thsii in the number List{}",nList)
    if(n<=1):
        return n
    for i in range(n-1):
        # print("Thiss in current index{}",i)
        # fibList.append(nList[i]+nList[i+1])
        fibList.append(fibList[i]+fibList[i+1])
    return fibList[n]


n = int(input())
print(calc_fib_fast(n))
# print(calc_fib(n))

