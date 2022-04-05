arr=[[0 for _ in range(7)] for _ in range(7)]

for i in range(0,7):
  arr[0][i]=10
  arr[i][0]=10
  arr[6][i]=10
  arr[i][6]=10
      

for i in range(1,6):
    line=list(map(int,input().split()))
    for j in range(5):
        arr[i][1+j]=line[j]

print(arr)
