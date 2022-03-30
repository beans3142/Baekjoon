from sys import stdin
input=stdin.readline

n,c=map(int,input().split())
vil=sorted([int(input()) for i in range(n)])
mn=1
mx=vil[-1]-vil[0]
ans=0
while mn<=mx:
    mid=(mx+mn)//2
    lastbuiltat=vil[0]
    totalbuilt=1
    for i in vil:
        if lastbuiltat+mid<=i:
            lastbuiltat=i
            totalbuilt+=1
    if c<=totalbuilt:
        ans=mid
        mn=mid+1
    else:
        mx=mid-1

print(ans)
