# Uses python3
import sys

def get_change(m):
    #write your code here
    number = 0
    count =0
    while(number<=m):
        if(number==m):
            return count
        if(number<m):
            if(number+10 <= m):
                number=number+10
                count=count+1
            elif(number+5 <=m):
                number=number+5
                count=count+1
            elif(number+1<=m):
                number=number+1
                count=count+1
    return m

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))


# m = int(input("Please Enter a nnumber"))
# print(m)
# print(get_change(m))
