from collections import deque
n=int(input())
arr=list(map(int,input().split()))
visited=[0]+[1000 for i in range(n-1)]
queue=deque([[arr[0],0,0]])
while queue:
    can,idx,tmpt=queue.popleft()
    for i in range(1,can+1):
        if idx+i<n:
            if tmpt+1<visited[idx+i]:
                visited[idx+i]=tmpt+1
                queue.append([arr[idx++i],idx+i,tmpt+1])
print(visited[-1] if visited[-1]!=1000 else -1)
