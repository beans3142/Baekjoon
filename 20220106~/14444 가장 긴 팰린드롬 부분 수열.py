from sys import stdin
from collections import defaultdict
input=stdin.readline
int(input())
dic=defaultdict(int)
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
            dic[i-a[i]+1,i+a[i]+1]=1
        if r<i+a[i]:
            r=i+a[i];
            p=i
    return a

w='_'+'_'.join(input().split())+'_'

ans=manach(w,len(w))

mx=0
ans_w=0

m=int(input())
for i in range(m):
    a,b=map(int,input().split())
    na=2*a-1
    nb=2*b-1
    print(int(ans[(na+nb)//2]>=b-a+1))
