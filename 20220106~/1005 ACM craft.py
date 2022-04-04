from sys import stdin
from collections import deque
input=stdin.readline

t=int(input())

for i in range(t):
    n,k=map(int,input().split())
    time={idx+1:i for idx,i in enumerate(list(map(int,input().split())))}
    dp={i:0 for i in range(1,n+1)}
    table={i:0 for i in range(1,n+1)}
    built={i:[] for i in range(1,n+1)}
    queue=deque([])

    for j in range(k):
        x,y=map(int,input().split())
        built[x].append(y)
        table[y]+=1

    for i in table:
        if table[i]==0:
             queue.append(i)
             dp[i]=time[i]

    while queue:
        building=queue.popleft()
        for i in built[building]:
            table[i]-=1
            dp[i]=max(dp[building]+time[i],dp[i])
            if table[i]==0:
                queue.append(i)
    ans=int(input())
    print(dp[ans])


        
