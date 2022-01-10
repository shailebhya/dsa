# Uses python3
def edit_distance(s, t):
    #write your code here
    m = len(s)
    n = len(t)
    results = [[0 for x in range(n + 1)] for x in range(m + 1)]
 
    for i in range(m + 1):
        for j in range(n + 1):
            #print('{},{}',m,n)
            if i == 0:
                results[i][j] = j   
            elif j == 0:
                results[i][j] = i
            elif s[i-1] == t[j-1]:
                results[i][j] = results[i-1][j-1]
            else:
                results[i][j] = 1 + min(results[i][j-1],       
                                   results[i-1][j],       
                                   results[i-1][j-1])    
 
    return results[m][n]
    # return 0

if __name__ == "__main__":
    print(edit_distance(input(), input()))

