import sys
from collections import deque
input=sys.stdin.readline

n,k=map(int,input().split())
arr=list(input().rstrip().split())

visited=set(''.join(arr))
queue=deque([[''.join(arr),0]])

ans=-1

while queue:
    arr,tmp=queue.popleft()
    arr=list(arr)
    
    if arr==sorted(arr):
        ans=tmp
        break

    for i in range(n-k+1):
        new_arr=arr
        print(arr,visited)
        s=new_arr[i:i+k]
        s.reverse()
        for j in range(k):
            new_arr[i+j]=s[j]
        new_arr=''.join(new_arr)
        if new_arr not in visited:
            visited.add(new_arr)
            queue.append([new_arr,tmp+1])

print(ans)
