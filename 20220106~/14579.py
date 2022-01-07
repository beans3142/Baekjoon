from sys import stdin
input=stdin.readline
a,b=map(int,input().split())
ans=1
now=a*(a+1)//2
for i in range(b-a+1):
    ans=ans*now%14579
    now=(now+a+1+i)%14579
print(ans)
