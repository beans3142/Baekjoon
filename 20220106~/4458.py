from sys import stdin
input=stdin.readline

n=int(input())
for i in range(n):
    s=input().rstrip()
    print(s[0].upper()+s[1:])
