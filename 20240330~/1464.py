from collections import deque
s=deque(input())
front=deque([])
le=len(s)
for i in range(le):
    now=s.popleft()
    if not front:
        front.append(now)
    else:
        if front[0]>=now:
            front=min(front,deque(reversed(front)))
            front.appendleft(now)
        else:
            front.append(now)
print(''.join(front))
