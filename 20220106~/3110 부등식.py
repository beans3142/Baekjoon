from fractions import Fraction
from sys import stdin
from collections import defaultdict
from bisect import bisect_left
input=stdin.readline

ans=0
case=[]
b,c,d=map(int,input().split())
a1,a2=map(int,input().split())
a=a1/a2
#a=Fraction(a1,a2)
e1,e2=map(int,input().split())
#e=Fraction(e1,e2)
e=e1/e2

for i in range(1,1001):
    #B=Fraction(i,b)
    B=i/b
    if e>B>a:
        for j in range(1,1001):
            #C=Fraction(j,c)
            C=j/c
            if B<C<e:
                case.append(C)

case.sort()

for i in range(1,1001):
    D=i/d
    #D=Fraction(i,d)
    if D<e:
        ans+=bisect_left(case,D)
    
print(ans)

# 중간것만 구하면 a< ? <c 와 c< ? <e 두 1차 부등식이 됨.
# 구현하기 귀찮아져서 다음에 다시 풀
