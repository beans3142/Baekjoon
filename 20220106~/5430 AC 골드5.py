import sys
from collections import deque
input=sys.stdin.readline
t=int(input())

for _ in range(t):
    try:
        order=input().rstrip()
        size=int(input())
        arr=deque(input().split(','))
        arr[0]=arr[0][1:]
        arr[-1]=arr[-1][:-2]
        rcount=0
        dcount=0
        for i in order:
            if i == 'R':
                rcount+=1
            else:
                dcount+=1
                if rcount%2==1:
                    arr.pop()
                else:
                    arr.popleft()
        if rcount%2==1 and arr:
            print('['+','.join(reversed(arr))+']')
        elif dcount<=size:
            print('['+','.join(arr)+']')
        else:
            print('error')
    except:
        print('error')
                
        
