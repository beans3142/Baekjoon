arr=[]
numList=[]
result=0
bingo=0

for _ in range(5):
  arr.append(list(map(int,input().split())))
  
for _ in range(5):
  numList+=list(map(int,input().split()))
  
for i in range(5):
  for j in range(5):
    for k in range(len(numList)):
      bingo=0
      if arr[i][j]==numList[k]:
        arr[i][j]=-1
        result+=1
        
        for m in range(5):
          if arr[m][0]==-1 and arr[m][1]==-1 and arr[m][2]==-1 and arr[m][3]==-1 and arr[m][4]==-1:
            bingo+=1
          
        for m in range(5):
          if arr[0][m]==-1 and arr[1][m]==-1 and arr[2][m]==-1 and arr[3][m]==-1 and arr[4][m]==-1:
            bingo+=1
          
        if arr[0][0]==-1 and arr[1][1]==-1 and arr[2][2]==-1 and arr[3][3]==-1 and arr[4][4]==-1:
          bingo+=1 
      
        if arr[0][4]==-1 and arr[1][3]==-1 and arr[2][2]==-1 and arr[3][1]==-1 and arr[4][0]==-1:
          bingo+=1
        
        if bingo==3 or bingo==4:
          print(result)
          exit()
 
