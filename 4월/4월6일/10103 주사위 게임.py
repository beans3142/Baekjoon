sca=scb=100

for i in range(int(input)):
    a,b=map(int,input().split())
    if a>b:
        scb-=a
    elif a<b:
        sca-=b

print(sca)
print(scb)
#https://www.acmicpc.net/problem/10103
