arr=[[10 for _ in range(7)] for _ in range(7)]
arr2=[list(map(int,input().split())) for i in range(5)]
tochange=[]

for i in range(5):
  for j in range(5):
    arr[1+i][1+j]=arr2[i][j]
    
for i in range(1,6):
  for j in range(1,6):
    if arr[i][j]<arr[i+1][j] and arr[i][j]<arr[i][j+1] and arr[i][j]<arr[i-1][j] and arr[i][j]<arr[i][j-1]:
      tochange.append([i,j])

for x,y in tochange:
    arr[x][y]='*'

for i in range(1,6):
  for j in range(1,6):
    print(arr[i][j],end=" ")
  print("")
