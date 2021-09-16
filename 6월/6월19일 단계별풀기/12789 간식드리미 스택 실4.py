from collections import deque

n=int(input())
people=deque(list(map(int,input().split())))
space=[]
nowturn=1

while nowturn<n:
    if space:
        if space[-1]==nowturn:
            space.pop()
            nowturn+=1
            continue
    if people:
        if people[0]==nowturn:
            people.popleft()
            nowturn+=1
            continue
    if people and space:
        nowperson=people.popleft()
        if nowperson < space[-1]:
            space.append(nowperson)
            continue
        else:
            print('Sad')
            exit()
    if people:
        space.append(people.popleft())
            
print('Nice')
