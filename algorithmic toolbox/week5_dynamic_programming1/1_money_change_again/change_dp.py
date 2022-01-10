# Uses python3
import sys

def get_change(m):
    #write your code here
    #1 3 4
    coins=[1,3,4]
    if m<=1:
        return m
    change = [0]*(m+1)
    change[0],change[1]=0,1
    for i in range(2,m+1):
        replaces =[]     
        for y in coins:
            if i==y:
                replaces.append(1)
            elif i>=y:
                replaces.append(change[i-y]+change[y])
            else:
                pass
        change[i]=min(replaces)
    return change[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
