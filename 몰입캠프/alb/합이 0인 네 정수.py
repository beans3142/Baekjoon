from sys import stdin
input=stdin.readline

n=int(input())
arr=[[] for i in range(4)]
for i in range(4):
    arr[i]=list(map(int,input().split()))

s1=set()
for i in range(n):
    for j in range(n):
        s1.add(arr[0][i]+arr[1][j])
a1=sorted(s1)

s2=set()
for i in range(n):
    for j in range(n):
        s2.add(arr[2][i]+arr[3][j])
a2=sorted(s2)

l=0
r=len(a2)-1

dif=float('inf')
ans=0

while True:
    s=a1[l]+a2[r]
    if abs(k-s)<dif:
        ans=s
        dif=abs(k-s)
    if l==len(a1)-1:
        break
    if r==0:
        break
    if abs(k-a1[l+1]-a2[r]) < abs(k-a1[l]-a2[r]):
        l+=1
    elif abs(k-a1[l]-a2[r-1]) < abs(k-a1[l]-a2[r]):
        r-=1
    else:
        l+=1
        r-=1

print(ans)
