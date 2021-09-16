#https://www.acmicpc.net/problem/15649
import sys

input=sys.stdin.readline

a,l=map(int,input().split())

def bt(idx,ls,v):
    queue=[[idx,ls,v]]
    while queue:
        depth,arr,V=queue.pop(0)
        if depth==l:
            print(' '.join(arr))
        else:
            for i in range(1,a+1):
                if V[i]==0 and str(i) not in arr:
                    nn=list(V)
                    nn[i]=1
                    queue.append([depth+1,arr+[str(i)],nn])

bt(0,[],[0]*(a+1))
