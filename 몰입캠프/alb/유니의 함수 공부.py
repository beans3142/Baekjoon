from sys import stdin
input=stdin.readline

l,r=map(int,input().split())

ans=r-l+1
for i in range(1,100):
    div=pow(2,i)
    if div>r:
        break
    ans+=((r//div-(l-1)//div)*(div//2))

print(ans)
