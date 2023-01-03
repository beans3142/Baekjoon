from sys import stdin
input=stdin.readline

for tc in range(int(input())):
    n,m,k=map(int,input().split())
    if n==m:
        if sum(map(int,input().split()))<k:
            print(1)
        else:
            print(0)
        continue
    home=2*list(map(int,input().split()))
    total=0
    ans=0
    for i in range(m):
        total+=home[i]
    if total<k:
        ans+=1
    for i in range(n-1):
        total+=home[m+i]
        total-=home[i]
        if total<k:
            ans+=1
    print(ans)
