from sys import stdin
from heapq import heappop,heappush
from collections import defaultdict
input=stdin.readline

prime=[1 for i in range(5000001)]
prime[0]=prime[1]=0

for i in range(2,int(5000000**0.5)):
    if prime[i]==1:
        for j in range(i*2,5000001,i):
            prime[j]=0
    

n=int(input())
대웅=[]
규성=[]
대웅점수=0
규성점수=0
말한소수=defaultdict(int)

for i in range(n):
    d_failed=g_failed=False
    d,g=map(int,input().split())
    if prime[d]==1:
        if 말한소수[d]!=0:
            대웅점수-=1000
        else:
            말한소수[d]=1
            heappush(대웅,-d)
    else:
        d_failed=True
    if d_failed:
        if len(규성)<3:
            규성점수+=1000
        else:
            임시저장=[]
            for j in range(3):
                임시저장.append(heappop(규성))
            규성점수-=임시저장[-1]
            for j in 임시저장:
                heappush(규성,j)
    if prime[g]==1:
        if 말한소수[g]!=0:
            규성점수-=1000
        else:
            말한소수[g]=1
            heappush(규성,-g)
    else:
        g_failed=True

    if g_failed:
        if len(대웅)<3:
            대웅점수+=1000
        else:
            임시저장=[]
            for j in range(3):
                임시저장.append(heappop(대웅))
            대웅점수-=임시저장[-1]
            for j in 임시저장:
                heappush(대웅,j)

if 규성점수>대웅점수:
    print("소수 마스터 갓규성")
elif 규성점수<대웅점수:
    print("소수의 신 갓대웅")
else:
    print("우열을 가릴 수 없음")
