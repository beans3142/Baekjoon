# 단순히 가운데에 휴게소를 지으면 안될 듯?
# ex) 0 1000 사이에 5개 짓기 => 무지성 가운데 짓기 => 500, 250, 125... 지만 최댓값은 250
#     0 1000 사이에 200,400,600,800... 이런식으로 200,200,200,200,200 으로 최대 200

# m개의 휴게소를 지을 수 있으므로 한 구간을 m이하로 나눈 값이 특정 값 이상 또는 이하라면
# 이런 식으로 전개해야 할 것?

# 생각해보니 좌표를 구할 필요는 전혀 없고 구간별 거리만 알고있으면 됨!!
# 구간별 거리를 우선순위 큐에 넣고 구간별 거리의 최댓값을 최댓값 이전의 값?
# 두번쨰로 큰 혹은 같은 값보다 작게 만들 m이하의 n을 구하면 됨
# n으로 나눈 뒤 n번 우선순위 큐에 다시 넣어주면 될 것 아마?

from sys import stdin
from heapq import heappop,heappush

input=stdin.readline

n,m,l=map(int,input().split())
locate=list(map(int,input().split())) if n!=0 else []
locate=[0]+locate+[l]

locate.sort()
length=[]


for i in range(len(locate)-1):
    key=locate[i+1]-locate[i]
    heappush(length,(-key,key,0,0))

while m:
    try:
        none,big,before,div=heappop(length)
        nextbig=length[0][1]
        boonmo=1
        if before:
            m-=1
            boonmo=div+1
            new_val=before/boonmo
            heappush(length,(-new_val,new_val,before,boonmo))
            continue
        while big/boonmo>=nextbig and m:
            boonmo+=1
            m-=1
        new_val=big/boonmo
        heappush(length,(-new_val,new_val,big,boonmo))
    except:
        print(big//m)
        exit()

print(int(length[0][1])+(length[0][1]%1!=0))
