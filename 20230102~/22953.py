# 시간복잡도의 계산 : N명의 요리사를 C번 고름 N**C 그 경우에 대해 알맞은 시간을 찾는 데 또 이진탐색 이용 logn
# N**C의 최댓값은 10**5로 백트래킹으로 간단히 해결 가능

from sys import stdin
input=stdin.readline

def checkcase():
    mintime=0
    maxtime=1000000**2
    while mintime<maxtime:
        mid=(mintime+maxtime)//2
        totalfood=0
        for i in range(n):
            totalfood+=mid//times[i]
        if totalfood<k:
            mintime=mid+1
        else:
            maxtime=mid
    return maxtime
        

def mkcase(idx,ccnt):
    global ans
    if ccnt<c:
        ans=min(ans,checkcase())
    if ccnt==c:
        ans=min(ans,checkcase())
        return
    for i in range(idx,n):
        if 1<times[i]:
            times[i]-=1
            mkcase(i,ccnt+1)
            times[i]+=1

    

n,k,c=map(int,input().split())
times=list(map(int,input().split()))
ans=1000000**2

mkcase(0,0)
print(ans)
