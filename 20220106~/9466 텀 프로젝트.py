from sys import stdin
from collections import defaultdict
input=stdin.readline

t=int(input())

for _ in range(t):
    n=int(input())
    arr=[0]+list(map(int,input().split()))
    dt=[0]*(n+1)
    cnt=0
    for i in range(1,n+1):
        if dt[i]==0:
            now=i
            dt[now]=1
            roop=defaultdict(int)
            roop[now]=1
            idx=1
            rooped=False
            while True:
                if roop[arr[now]]!=0:
                    rooped=True
                    break
                if dt[arr[now]]!=0:
                    break
                idx+=1
                roop[arr[now]]=idx
                dt[arr[now]]=1
                now=arr[now]
            if rooped==False:
                cnt+=len(roop)-1
            else:
                cnt+=len(roop)-(roop[now]-roop[arr[now]]+1)
    print(cnt)
