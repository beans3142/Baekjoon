from sys import stdin
input=stdin.readline


n=int(input())
x=0
p=map(int,input().split())
for i in p:
    x^=i
if x:
    print('koosaga')
else:
    print('cubelover')
