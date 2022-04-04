#https://www.acmicpc.net/problem/2577

a=int(input())
b=int(input())
c=int(input())

total=a*b*c

for i in range(0,10):
    print(str(total).count(str(i)))
