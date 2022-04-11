from sys import stdin
input=stdin.readline

l,r=map(int,input().split())

ans=r-l+1
for i in range(1,100):
    div=2**i
    if div>r:
        break
    mok=r//div-(l-1)//div
    add=mok*(div//2)
    ans+=add

print(ans)
