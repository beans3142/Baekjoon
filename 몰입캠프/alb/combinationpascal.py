arr=[[0 for i in range(31)] for j in range(31)]
for i in range(31):
    arr[i][0]=arr[i][i]=1

for i in range(31):
    for j in range(1,i):
        arr[i][j]=arr[i-1][j]+arr[i-1][j-1]
    
n,m=map(int,input().split())
print(arr[n][m])
