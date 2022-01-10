# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_fast(a,b):
    current_gcd= 1
    while b!=0:
        current_gcd=a%b
        a=b
        b=current_gcd

    return a
    

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    # print(gcd_naive(a, b))
    print(gcd_fast(a,b))

# # a, b = map(int, input.split())
# a=int(input())
# b=int(input())
# print(gcd_naive(a, b))
# print(gcd_fast(a,b))