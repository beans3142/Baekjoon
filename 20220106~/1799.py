from time import *
from sys import *
setrecursionlimit(100000)
input=stdin.readline

n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
now=time()
dp=[[0 for i in range(n)] for i in range(n)]
loc=[[0 for i in range(n)] for i in range(n)]
ans=0
able=0
recur=0
for i in range(n):
    for j in range(n):
        able+=arr[i][j]

def bt(x,y,cnt,left):
    global ans#,recur
    #recur+=1
    if ans<cnt:
        ans=cnt
        '''
        for i in loc:
            print(i)
        print(left)
        '''
    if y==n:
        return
    for i in range(y,n):
        for j in range(x,n):
            if arr[i][j]==1 and dp[i][j]==0:
                rmv=fill(j,i,1)
                #loc[i][j]=1
                if not (cnt+left<ans):
                    if j+1==n:
                        bt(0,i+1,cnt+1,left-rmv)
                    else:
                        bt(j+1,i,cnt+1,left-rmv)
                #loc[i][j]=0
                fill(j,i,-1)


        
def fill(x,y,d):
    rmv=0
    for i in range(1,n):
        if x+i==n or y+i==n:
            break
        if arr[y+i][x+i]==1 and dp[y+i][x+i]==0:
            rmv+=1
        dp[y+i][x+i]+=d


    for i in range(1,n):
        if x-i==-1 or y+i==n:
            break
        if arr[y+i][x-i]==1 and dp[y+i][x-i]==0:
            rmv+=1
        dp[y+i][x-i]+=d


    for i in range(1,n):
        if x-i==-1 or y-i==-1:
            break
        dp[y-i][x-i]+=d

    for i in range(1,n):
        if x+i==n or y-i==-1:
            break
        dp[y-i][x+i]+=d
        

    dp[y][x]+=d
    return rmv+1


bt(0,0,0,able)

print(ans)
print(time()-now)
print(recur)

'''
7
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1

8
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
'''
