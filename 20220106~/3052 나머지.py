#https://www.acmicpc.net/problem/3052

nl=[]

for i in range(0,10):
    n=int(input())%42
    if n not in nl:
        nl.append(n)

print(len(nl))
