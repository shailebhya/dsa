# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def get_fibonacci_last_digit_fast(n):
    if n<=1:
        return n
    
    last_digit = 1
    pLast_digit=0

    for _ in range(n-1):
        pLast_digit,last_digit=last_digit,(last_digit+pLast_digit)%10

    return last_digit


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    # print(get_fibonacci_last_digit_naive(n))
    print(get_fibonacci_last_digit_fast(n))


# n = int(input())
# print(get_fibonacci_last_digit_naive(n))
# print(get_fibonacci_last_digit_fast(n))