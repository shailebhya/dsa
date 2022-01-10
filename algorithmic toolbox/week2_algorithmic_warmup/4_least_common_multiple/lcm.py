# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def gcd_fast(a,b):
    current_gcd= 1
    while b!=0:
        current_gcd=a%b
        a=b
        b=current_gcd
    return a

def lcm_fast(a,b):
    if a ==0 or b == 0:
        return 0
    return (a*b)//gcd_fast(a,b)
    

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    # print(lcm_naive(a, b))
    print(lcm_fast(a,b))

# a,b = int(input()),int(input())
# print(lcm_naive(a, b))
# print(lcm_fast(a,b))
