from sys import stdin
input=stdin.readline

n,k=map(int,input().split())
arr=[input().rstrip() for i in range(n)]
cnt=0

for i in range(2*k):
    se=set()
    for j in range(n):
        se.add(arr[j][i])
    cnt+=len(se)
    print(len(se))

print(cnt)
