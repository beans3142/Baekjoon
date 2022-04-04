import sys
input=sys.stdin.readline

dots=[list(map(int,input().split()))for i in range(3)]

s=((dots[1][0]-dots[0][0])*(dots[2][1]-dots[0][1])\
   -(dots[1][1]-dots[0][1])*(dots[2][0]-dots[0][0]))/2

if s>0:
    print(1)
elif s==0:
    print(0)
else:
    print(-1)
