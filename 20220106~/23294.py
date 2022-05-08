from sys import stdin
from collections import deque,defaultdict
input=stdin.readline

inf=float('inf')

n,q,c=map(int,input().split())
cap=list(map(int,input().split()))

back=deque([])
front=deque([])
nowc=0
now=inf

for i in range(q):
    order=input().rstrip()
    if order=='B':
        if not back:
            continue
        front.appendleft(now)
        now=back.pop()
        #nowc-=cap[now-1]
    elif order=='F':
        if not front:
            continue
        back.append(now)
        now=front.popleft()
        #nowc-=cap[now-1]
    elif order=='C':
        vi=defaultdict(int)
        le=len(back)
        bef=inf
        for j in range(le):
            nowback=back.pop()
            if bef==nowback:
                nowc-=cap[nowback-1]
                continue
            bef=nowback
            vi[nowback]=1
            back.appendleft(nowback)
    else:
        t,loc=order.split()
        loc=int(loc)
        if now!=inf:
            #nowc+=cap[now-1]
            back.append(now)
        now=loc
        nowc+=cap[loc-1]
        for j in front:
            nowc-=cap[j-1]
        front=deque([])
        '''
        if nowc>c:
            if back:'''
        while nowc>c:
            lastb=back.popleft()
            nowc-=cap[lastb-1]
    #print(i+1,'\t',order,'\t',back,now,front,nowc)
               
print(now)
back.reverse()

if back:
    print(*back)
else:
    print(-1)
if front:
    print(*front)
else:
    print(-1)
        

'''
2 7 5
1 1
A 1
A 2
A 1
A 2
A 1
B
B
'''
