from sys import stdin
input=stdin.readline
n,m=map(int,input().split())
for i in range(n):
    a,b=map(int,input().split())
    if a!=b:
        print('Wrong Answer')
        exit()
for i in range(m):
    a,b=map(int,input().split())
    if a!=b:
        print('Why Wrong!!!')
        exit()
print('Accepted')
