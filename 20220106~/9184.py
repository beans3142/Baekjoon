'''
if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    '''

dp=[[[0]*21 for i in range(21)] for j in range(21)]
dp[0][0][0]=1
def recur(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    elif a<b<c:
        if dp[a][b][c]!=0:
            return dp[a][b][c]
        val=recur(a,b,c-1)+recur(a,b-1,c-1)-recur(a,b-1,c)
        dp[a][b][c]=val
        return val
    else:
        if dp[a][b][c]!=0:
            return dp[a][b][c]
        val=recur(a-1,b,c)+recur(a-1,b-1,c)+recur(a-1,b,c-1)-recur(a-1,b-1,c-1)
        dp[a][b][c]=val
        return val
        
recur(20,20,20)

while True:
    a,b,c=map(int,input().split())
    if a==b==c==-1:
        break
    print(f'w{a,b,c} = ',end='')

    if a<=0 or b<=0 or c<=0:
        a,b,c=0,0,0
    elif a>20 or b>20 or c>20:
        a,b,c=20,20,20

    if dp[a][b][c]:
        print(dp[a][b][c])
    else:
        recur(a,b,c)
        print(dp[a][b][c])
