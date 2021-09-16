from sys import stdin
input=stdin.readline

# 1~15
# 16 ~ 31

n=int(input())

for i in range(n):
    s=int(input())
    ans=(15-s%15) if s//15%2 == 1 else (s%15 if s%15!= 0 else 15)
    ans=bin(ans+(2**32))
    for j in range(4):
        print('V' if ans[-4+j]=='0' else '딸기',end='')
    print()
