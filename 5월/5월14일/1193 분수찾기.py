#https://www.acmicpc.net/problem/1193

x=int(input())
i=1

while True:
    x-=i
    if x<=0:
        break
    i+=1

if i%2==0:
    print(f'{i+x}/{1-x}')
else:
    print(f'{1-x}/{i+x}')
