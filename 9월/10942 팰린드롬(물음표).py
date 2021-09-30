from sys import stdin
input=stdin.readline

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

n=int(input())
w='0 '+' 0 '.join(input().rstrip().split())+' 0'
w=w.split()

ans=manach(w,len(w))

m=int(input())
for i in range(m):
    a,b=map(int,input().split())
    A=2*a-1
    B=2*b-1
    mid=(A+B)//2
    if b-a+1<=ans[mid]:
        print(1)
    else:
        print(0)
