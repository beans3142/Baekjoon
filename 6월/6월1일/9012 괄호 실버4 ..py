#https://www.acmicpc.net/problem/9012

import sys
input=sys.stdin.readline

for i in [list(input().rstrip()) for i in range(int(input()))]:
    is_vps=0
    for j in i:
        if j=='(':
            is_vps+=1
        elif j==')':
            is_vps-=1
        if is_vps<0:
            break
    if is_vps==0:
        print('YES')
    else:
        print('NO')
            
    
