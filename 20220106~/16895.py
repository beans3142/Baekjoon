n=int(input())
p=list(map(int,input().split()))

cnt=0
for i in range(n):
    x=0
    for j in range(n):
        if j==i:
            continue
        x^=p[j]
    for j in range(p[i]):
        if x^j==0:
            cnt+=1
print(cnt)
