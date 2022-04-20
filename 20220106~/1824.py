from sys import stdin
from collections import defaultdict
input=stdin.readline

def show():
    for i in range(n):
        for j in range(m):
            print(placed[i*m+j+1],end=' ')
        print()
    print()

def dfs(x):
    if vi[x]:
        return False
    vi[x]=True
    for i in able[x]:
        if placed[i]==0 or dfs(placed[i]):
            vi[i]=True
            placed[i]=x
            return True

    return False
    

n,m=map(int,input().split())
able=[[] for i in range(n*m+1)]
arr=[[m*j+i for i in range(1,m+1)] for j in range(n)]

for i in range(n):
    for j in range(m-1):
        if (i+j)%2==0:
            able[arr[i][j]].append(arr[i][j+1])
        else:
            able[arr[i][j+1]].append(arr[i][j])

for i in range(n-1):
    for j in range(m):
        if (i+j)%2==0:
            able[arr[i][j]].append(arr[i+1][j])
        else:
            able[arr[i+1][j]].append(arr[i][j])

''' 
for i in range(1,n):
    for j in range(n):
        able[arr[i-1][j]].append(arr[i-1][j])'''

l=int(input())
for i in range(l):
    a,b=map(int,input().split())
    able[a]=[i for i in able[a] if i!=b]
    able[b]=[i for i in able[b] if i!=a]

#for _ in range(len(able[1])):

vi=[False]*(n*m+1)
placed=[0]*(n*m+1)
mx=n*m
#for i in range(1,n*m+1):

for i in range(1,n*m+1):
    for j in range(1,n*m):
        vi[j]=False
    dfs(i)

for i in range(n):
    for j in range(m):
        if (i+j)%2:
            print(i*m+j+1,placed[i*m+j+1])
