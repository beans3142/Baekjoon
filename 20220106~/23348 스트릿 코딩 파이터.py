a,b,c=map(int,input().split())
n=int(input())

ans=0

for i in range(n):
    score=0
    for j in range(3):
        n,m,k=map(int,input().split())
        score+=a*n+b*m+c*k
    ans=max(score,ans)

print(ans)
