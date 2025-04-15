from sys import stdin
input=stdin.readline
n=int(input())
dd=dict()
s=[0]
for i in range(1,n+1):
    dd[i]=[i]
    s.append(input().rstrip())
for i in range(n-1):
    a,b=map(int,input().split())
    dd[a].append(dd[b])
    del dd[b]
for i in dd:
    ans=str(d
    for j in ans:
        if '[' in j or ']' in j:
            continue
        else:
            print(s[int(j)],end='')
