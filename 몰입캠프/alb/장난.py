from sys import stdin
from collections import defaultdict
input=stdin.readline

n=int(input())
difs=sorted(list(map(int,input().split())))
dif=defaultdict(int)

for i in difs:
    dif[i]+=1
    
arr=[]

def bt(x):
    arr.append(x)
    if len(arr)==n:
        print(*arr)
        exit()
    for j in difs:
        if dif[j]==0:
            continue
        able=True
        li=defaultdict(int)
        li[j]+=1
        for i in range(1,len(arr)):
            num=arr[i]
            d=abs(num-j)
            if not(d in dif and dif[d]):
                able=False
                break
            li[d]+=1
        if able:
            able2=True
            for k in li:
                if k not in dif:
                    able2=False
                    break
                if li[k]>dif[k]:
                    able2=False
                    break
            if able2:
                for k in li:
                    dif[k]-=li[k]
                bt(j)
                arr.pop()
                for k in li:
                    dif[k]+=li[k]

    
bt(0)
