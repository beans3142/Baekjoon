#https://www.acmicpc.net/problem/14681

x=int(input())
y=int(input())

print((x<0)*(2*(y>0)+3*(y<0))+(x>0)*(1*(y>0)+4*(y<0)))
