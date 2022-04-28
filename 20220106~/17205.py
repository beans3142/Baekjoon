from sys import stdin
input=stdin.readline

n=int(input())
s=input().rstrip()
ans=0

for i in range(len(s)):
    sw=ord(s[i])-97
    add=sum([sw*26**(n-1-j) for j in range(n)])+1
    n-=1
    ans+=add

print(ans)
