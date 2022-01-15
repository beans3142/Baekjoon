from sys import stdin
input=stdin.readline

n=int(input())
for i in range(n):
    s=input().rstrip()
    if s[len(s)//2-1]==s[len(s)//2]:
        print('Do-it')
    else:
        print('Do-it-Not')
