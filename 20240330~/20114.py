from sys import stdin
input=stdin.readline

n,h,w=map(int,input().split())
s=[input().rstrip() for i in range(h)]
wonbon=['' for i in range(n)]
for j in range(h):
    for k in range(n):
        wonbon[k]+=s[j][w*k:w*(k+1)]

for i in wonbon:
    if set(i)-{"?"}:
        for i in set(i)-{"?"}:
            print(i,end="")
    else:
        print("?",end="")
    