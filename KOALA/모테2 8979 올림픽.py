import sys
input=sys.stdin.readline
n,k=map(int,input().split())
arr=sorted([list(map(int,input().split())) for _ in range(n)])
key=tuple(arr[k-1][1:])
arr=list(map(lambda x: x[1:],arr))
rank={}
now_rank=0
for i in sorted(arr,reverse=True):
    try:
        rank[tuple(i)][1]+=1
        now_rank+=1
    except:
        rank[tuple(i)]=[now_rank,0]
        now_rank+=1

print(rank[key][0]+1)

#1 2 3 4
