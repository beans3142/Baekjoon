from collections import defaultdict
N=int(input())

arr=list(map(int,input().split()))
cnt=defaultdict(int)
valid=0
  
for i in arr:
  cnt[i]+=1
  
for i in cnt:
  if cnt[i]<2:
    valid+=cnt[i]
  else:
    valid+=2
    
if valid>=6:
  print("YES")
else:
  print("NO")
  
