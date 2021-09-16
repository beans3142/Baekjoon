from collections import *

t=int(input())
a=list(map(int,input().split()))
math=list(map(int,input().split()))#0 : +, 1 : -, 2 : *, 3 : //
mx=-10000000001
mn=10000000001

def op(cnt,result,p,m,mul,div):
    global mx,mn
    if cnt==t:
        mx=max(result,mx)
        mn=min(mn,result)
    if p:
        op(cnt + 1, result + a[cnt], p - 1, m, mul, div)
    if m:
        op(cnt + 1, result - a[cnt], p, m - 1, mul, div)
    if mul:
        op(cnt + 1, result * a[cnt], p, m, mul - 1, div)
    if div:
        op(cnt + 1, -(-result // a[cnt]) if result < 0 else result // a[cnt], p, m, mul, div - 1)


op(1,a[0],math[0],math[1],math[2],math[3])

print(mx)
print(mn)
