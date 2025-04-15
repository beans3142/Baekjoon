from sys import stdin
input=stdin.readline
int(input())
def manach(s,n):
    a=[0]*n
    r=p=0
    for i in range(n):
        if i<=r:
            a[i]=min(a[2*p-i],r-i)
        else:
            a[i]=0
        while (i-a[i]-1>=0 and i+a[i]+1<n and s[i-a[i]-1]==s[i+a[i]+1]):
            a[i]+=1
        if r<i+a[i]:
            r=i+a[i];
            p=i
    return a

w=list(input().rstrip())
nw=[0]*(2*len(w)+1)
for i in range(len(w)):
    nw[1+2*i]=w[i]

arr=manach(nw,len(nw))

mx=0
ans=len(arr)

for i in range(len(arr)):
    if i+arr[i]==len(arr)-1:
        ans=min(ans,(len(arr)-1)//2-arr[i])

print(ans)
