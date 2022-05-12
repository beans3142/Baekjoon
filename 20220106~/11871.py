n=int(input())
p=list(map(int,input().split()))

x=0
for i in range(n):
    x^=(p[i]+1)//2 if p[i]%2 else (p[i]-1)//2

if x:
    print('koosaga')
else:
    print('cubelover')
