from collections import deque
n,k=map(int,input().split())
big=max(n,k)*2
matrix=[100001]*big

queue=deque([[n,0]])
cnt=0

while queue:
    now,tmpt=queue.popleft()
    if now==k:
        matrix[k]=tmpt
        cnt+=1
    else:
        try:
            if now>big*2:
                continue
            if now<k and tmpt<matrix[now+1]:
                matrix[now+1]=tmpt+1
                queue.append([now+1,tmpt+1])
            if 0<now<big and tmpt<matrix[now-1]:
                matrix[now-1]=tmpt+1
                queue.append([now-1,tmpt+1])
            if now<k and tmpt<matrix[now*2]:
                matrix[now*2]=tmpt+1
                queue.append([now*2,tmpt+1])
        except:
            pass

print(matrix[k])
print(cnt)
