from sys import stdin
input=stdin.readline
n=int(input())
inequals=input().rstrip().split()
used=[0]*10
mn=0
mx=0

def dfs(le,num):
    global mn,mx
    if le==n:
        if mn==0:
            mn=[*ans]
        mx=[*ans]
        return
    if inequals[le]=='<':
        for i in range(num+1,10):
            if used[i]==0:
                used[i]=1
                ans.append(i)
                dfs(le+1,i)
                ans.pop()
                used[i]=0
    else:
        for i in range(0,num):
            if used[i]==0:
                used[i]=1
                ans.append(i)
                dfs(le+1,i)
                ans.pop()
                used[i]=0

                 
for i in range(10):
    used[i]=1
    ans=[i]
    dfs(0,i)
    used[i]=0

print(*mx,sep='')
print(*mn,sep='')
