## template

n=int(input())
result=[0]*100
resultLen=0
isFinished=False

def isPossible(x,length):
  for i in range(length):
    if result[x-i]!=result[x-i-length]:
      return True
  return False


def getResult(x):
  global isFinished
  if(isFinished==True):
    exit()
  
  if(x>=n):
    for i in range(n):
      print(result[i],end='')
      isFinished=True
    exit()
  
  for i in range(1,4):
    result[x]=i 
    
    flag=False
    for j in range(1,(x+1)//2+1):
      if not isPossible(x,j):
        flag=True
        break

    if flag==False:
      getResult(x+1)
      
getResult(0)








