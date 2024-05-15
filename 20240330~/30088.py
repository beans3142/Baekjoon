from sys import stdin
input=stdin.readline

n=int(input())
s=[]
for i in range(n):
    s.append(sum(list(map(int,input().split()))[1:]))
    
s.sort()
t=0
for i in range(n):
    t+=s[i]*(n-i)
print(t)
