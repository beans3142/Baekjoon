## template
from collections import defaultdict

N,K=map(int,input().split())
arr=list(map(int,input().split()))
result=defaultdict(int)
cnt=0
sum=0

for i in range(len(arr)):
  sum+=arr[i]
  result[sum]+=1

for key in result:
  value=result[key]
  num=i-K
  if num in result:
    cnt+=i[1]

print(cnt)
