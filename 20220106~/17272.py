from sys import stdin
input = stdin.readline

divby=1000000007

n,m=map(int,input().split())


def mm(first,second):
    ans = [[0]*(m+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,m+1):
            for k in range(1,m+1):
                ans[i][j] += first[i][k] * second[k][j]
            ans[i][j] %= divby
    return ans

def sol(n):
    if n==1:
        return matrix
    now=sol(n//2)
    ans=mm(now,now)
    if n%2:
        ans=mm(matrix,ans)
    return ans
    

matrix=[[0]*(m+1) for i in range(m+1)]
matrix[1][1]=matrix[1][-1]=1
for i in range(1,m):
    matrix[i+1][i]=1

ans=sol(n)
print(ans[1][1])
