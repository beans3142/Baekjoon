from sys import stdin
input = stdin.readline

divby=1000000007

n = int(input())


def mm(*info):
    
    if len(info)==1:
        first=second=info[0]
    else:
        first=info[0]
        second=info[1]
        
    ans = [[0] * len(first) for _ in range(len(first))]
    for i in range(len(first)):
        for j in range(len(first)):
            for k in range(len(first)):
                ans[i][j] += first[i][k] * second[k][j]
            ans[i][j] %= divby
    return ans

if n%2==0:
    n//=2
    n-=1
    matrix = [[4, -1], [1, 0]]
    x = [[1, 0], [0, 1]]
    while n > 0:
        if n%2:
            x = mm(matrix, x)
        n >>= 1
        matrix = mm(matrix)
    print((3 * x[0][0] + x[0][1]) % divby)
else:
    print(0)
