n=int(input())
arr=[[*map(int,input().split())] for i in range(n)]
same=[[0 for i in range(n)] for i in range(n)]
for i in range(5):
  for j in range(n):
    for k in range(n):
      if j==k:
        continue
      if arr[j][i]==arr[k][i]:
        same[j][k]=same[k][j]=1

president=1
maxsametime=1
for i in range(n):
  sametime=sum(same[i])
  if maxsametime<sametime:
    maxsametime=sametime
    president=i+1

print(president)
