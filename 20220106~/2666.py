from sys import stdin
from copy import deepcopy
input=stdin.readline

n=int(input())
opened=[*map(int,input().split())]
dp=[[[1]*(n),0]]
for i in opened:
    dp[0][0][i-1]=0 # 닫힘 1 열림 0

m=int(input())
for i in range(m):
    no=int(input())-1
    ndp=[]
    for i in dp:
        if i[0][no]==0:
            ndp.append(i)
        else:
            # 왼쪽으로 밀어서 열기
            nowcnt=i[1]
            li=deepcopy(i[0])
            cnt=0
            for idx in range(no,n):
                if li[idx]==0:
                    li[idx],li[no]=li[no],li[idx]
                    ndp.append([li,nowcnt+cnt])
                    break
                else:
                    cnt+=1
            # 오른쪽으로 밀어서 열기
            ri=deepcopy(i[0])
            cnt=0
            for idx in range(no,-1,-1):
                if ri[idx]==0:
                    ri[idx],ri[no]=ri[no],ri[idx]
                    ndp.append([ri,nowcnt+cnt])
                    break
                else:
                    cnt+=1
    dp=ndp

mn=10**9
for i in dp:
    mn=min(mn,i[1])

print(mn)
