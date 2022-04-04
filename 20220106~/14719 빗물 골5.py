# ㅈㄴ 마음에 들게 된 코드

import sys
input=sys.stdin.readline

h,w=map(int,input().split())
l=list(map(int,input().split()))

matrix=[['■'*(max(l)-j<=i) or '□' for i in l] for j in range(max(l))]

water=0

for i in matrix:
    block=[]
    for a in range(len(i)):
        if i[a] == '■':
            block.append(a)
    if len(block)>1:
        for i in range(1,len(block)):
            water+=block[i]-block[i-1]-1

print(water)
