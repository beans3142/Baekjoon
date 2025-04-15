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

w=input().rstrip().split()
nw=[0]*(2*len(w)+1)
for i in range(len(w)):
    nw[1+2*i]=w[i]

ans=manach(nw,len(nw))

mx=0
ans_w=0

m=int(input())
for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    print(1 if ans[a+b+1]>=b-a+1 else 0)
