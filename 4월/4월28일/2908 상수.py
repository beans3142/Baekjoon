#https://www.acmicpc.net/problem/2908

a,b=map(int,input().split())

a=a%10*100+(a-a//100*100-a%10)+a//100
b=b%10*100+(b-b//100*100-b%10)+b//100

print(max(a,b))
