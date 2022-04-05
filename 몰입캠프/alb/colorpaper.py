n=int(input())
arr=[[0 for i in range(101)] for i in range(101)]
for i in range(1,n+1):
    x,y,w,h=map(int,input().split())
    for j in range(w):
        for k in range(h):
            arr[~(y+k)][x+j]=i

tile=[0]*n
for i in range(101):
    for j in range(101):
        if arr[i][j]!=0:
            tile[arr[i][j]-1]+=1

for i in tile:
    print(i)
    
