from sys import stdin
input=stdin.readline

n=int(input())
skills=input().rstrip()
scnt=0
lcnt=0
ans=0

for i in range(n):
    if '1'<=skills[i]<='9':
        ans+=1
    elif skills[i]=='S':
        scnt+=1
    elif skills[i]=='L':
        lcnt+=1
    elif skills[i]=='K':
        if scnt>0:
            scnt-=1
            ans+=1
        else:
            break
    else:
        if lcnt>0:
            lcnt-=1
            ans+=1
        else:
            break

print(ans)
