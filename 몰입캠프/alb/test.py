arr=[]
num=[]
bingo=0

for _ in range(5):
  arr.append(list(map(int,input().split())))

for _ in range(5):
  num+=list(map(int,input().split()))


for k in range(len(num)):
  for i in range(5):
    for j in range(5):
      cnt=0
      if arr[i][j]==num[k]:
        arr[i][j]=-1
        bingo+=1

      for m in range(5):
        xcnt=0
        for n in range(5):
          if arr[m][n]==-1:
            xcnt+=1
        if xcnt==5:
          cnt+=1

      for m in range(5):
        ycnt=0
        for n in range(5):
          if arr[n][m]==-1:
            ycnt+=1
        if ycnt==5:
          cnt+=1

      if arr[0][0]==-1 and arr[1][1]==-1 and arr[2][2]==-1 and arr[3][3]==-1 and arr[4][4]==-1:
        cnt+=1

      if arr[0][4]==-1 and arr[1][3]==-1 and arr[2][2]==-1 and arr[3][1]==-1 and arr[4][0]==-1:
        cnt+=1

      if cnt>=3:
        print(bingo)
        exit()
      
