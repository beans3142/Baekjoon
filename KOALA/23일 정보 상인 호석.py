from heapq import heappush,heappop
from sys import stdin
input=stdin.readline

q=int(input())
total=0
shopkeeper={}
for i in range(q):
    order=input().rstrip().split()
    if order[0]=='1':
        try:
            for i in range(3,len(order)):
                heappush(shopkeeper[order[1]],-int(order[i]))
        except:
            shopkeeper[order[1]]=[]
            for i in range(3,len(order)):
                heappush(shopkeeper[order[1]],-int(order[i]))
    else:
        #print(shopkeeper)
        try:
            cnt=int(order[2])
            if len(shopkeeper[order[1]])<=cnt:
                total-=sum(shopkeeper[order[1]])
                shopkeeper[order[1]]=[]
            else:
                for i in range(cnt):
                    total-=heappop(shopkeeper[order[1]])
        except:
            pass
        #print('after',shopkeeper)

print(total)
