n=int(input())
rn=0
while n:
    rn+=n%10
    rn*=10
    n//=10
rn//=10
