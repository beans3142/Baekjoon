from sys import setrecursionlimit
setrecursionlimit(10000)
def tobin(now,le,cnt):
    if le==n:
        if cnt==k:
            print(now)
        return
    if cnt<k:
        tobin(now+'1',le+1,cnt+1)
    tobin(now+'0',le+1,cnt)
    

n,k=map(int,input().split())
tobin('',0,0)

'''
짧은 것 처리
in 
1 0

out
0

in
1 1

out
1

기타 체크용
in
5 0

out
00000

in
7 7

out
1111111
'''
