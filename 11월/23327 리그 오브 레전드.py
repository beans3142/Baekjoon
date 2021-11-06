from sys import stdin
input=stdin.readline

n,q=map(int,input().split())
arr=list(map(int,input().split()))
s=[0]
s2=[0]

for i in range(n):
    s.append(s[-1]+arr[i])
    s2.append(s2[-1]+arr[i]**2)

for i in range(q):
    l,r=map(int,input().split())
    ab=s[r]-s[l-1]
    aa=s2[r]-s2[l-1]
    print((ab**2-aa)//2)
