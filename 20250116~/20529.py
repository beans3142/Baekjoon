from sys import stdin;input=stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    s=input().rstrip().split()
    if n>=48:
        print(0)
        continue
    ans=1e10
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                ans=min(ans,len(set(s[i]+s[j]))+len(set(s[i]+s[k]))+len(set(s[j]+s[k]))-12)
    print(ans)