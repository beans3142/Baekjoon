''' 수정 전 코드인데 뭔가 가능은 할 것 같은데..
import sys
input=sys.stdin.readline

t=int(input())

for i in range(t):
    case=int(input())
    clothes={}
    total=0
    for j in range(case):
        _kind,_type=input().rstrip().split()
        try:
            total+=total//clothes[_type]-len(clothes)+1
            clothes[_type]+=1
        except:
            total+=total+1
            clothes[_type]=1
    print(total)
'''

import sys
input=sys.stdin.readline

t=int(input())

for i in range(t):
    case=int(input())
    clothes={}
    total=1
    for j in range(case):
        _kind,_type=input().rstrip().split()
        try:
            clothes[_type]+=1
        except:
            clothes[_type]=1
    for i in clothes:
        total*=clothes[i]+1
    print(total-1)
