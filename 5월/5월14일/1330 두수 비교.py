#https://www.acmicpc.net/problem/1330

a,b=map(int,input().split())

print('<'*(a<b)+'>'*(a>b)+'=='*(a==b))
