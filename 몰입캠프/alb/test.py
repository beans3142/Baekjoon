## template
from collections import deque

n=int(input())
check=[-1]*1000000
check[1]=0

def bfs():
  global n
  arr=deque()
  arr.append(1)
  
  while not len(arr)==0:
    x=arr.popleft()
    
    myVal=x*2
    if myVal>=1 and myVal<=99999 and check[myVal]==-1:
      check[myVal]=check[x]+1
      arr.append(myVal)
      if myVal==n:
        break
      
    myVal=x//3
    if myVal>=1 and myVal<=99999 and check[myVal]==-1:
      check[myVal]=check[x]+1
      arr.append(myVal)
      if myVal==n:
        break
      
bfs()
print(check[n])
