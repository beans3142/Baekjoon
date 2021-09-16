#https://www.acmicpc.net/problem/12906

#1 '최소'로 움직이려면?
# 모든 경우 다 돌아보려면?
# 한 막대에서 옮길수 있는 선택지 2개
# 막대 개수 3개
# 6**10?

# 풀이?

#1)
# bfs로 돌리다 맨 처음에 입력받은 A개수 B개수 C개수와
# 1,2,3 막대에 들어있는 것들의 개수가 모두 같으면 이게 답인지 확인

# bfs로 하면 확정적으로 정답(최소)을 구할 수 있을 것 (아마도),

#1-1)
# 
# bfs 결과 다 담아놓고 정렬
# 막대에는 빈 공간에 'AA' 이렇게 채워줘서 정렬시에 AAA BBB CCC 순서로 올 것.

#2)
# 가장 효율적인 방법?
# 바닥부터 완성시키는 것, 1번 막대 맨 밑에 있는 연속된 a는 움직일 필요가 없음

#2-1)
# 한쪽으로 다 옮기고 (하나를 비우고) 두 막대 중 하나를 골라서
# 남은 하나에 옮기면서 빈 막대에 해당하는 값을 옮겨

#2-1-1)
# 가장 적은 수를 가진 쪽으로 모두 옮긴 뒤 정리?
# 2 4 4 있으면 2를 다 옮긴 뒤 진행 이런식..

# 문자열을 하나로 합치고 길이를 이용할수 있을까?
# AABBCAC 이런식으로..

from collections import deque
from sys import stdin
input=stdin.readline

visited={}
arr=[]
num_a=num_b=num_c=0

for i in range(3):
    line=input().rstrip()
    arr.append('' if len(line)==1 else line.split()[1])
    num_a+=arr[i].count('A')
    num_b+=arr[i].count('B')
    num_c+=arr[i].count('C')

last=('A'*num_a if num_a>0 else '',\
      'B'*num_b if num_b>0 else '','C'*num_c if num_c>0 else '')

def bfs(stick_a,stick_b,stick_c):
    queue=deque([[stick_a,stick_b,stick_c,0]])
    visited[(stick_a,stick_b,stick_c)]=0
    while queue:
        a,b,c,tmpt=queue.popleft()
        if a:
            top=a[-1]
            l=a[:len(a)-1]
            try:
                visited[(l,b+top,c)]
            except:
                visited[(l,b+top,c)]=tmpt+1
                queue.append([l,b+top,c,tmpt+1])
            try:
                visited[(l,b,c+top)]
            except:
                visited[(l,b,c+top)]=tmpt+1
                queue.append([l,b,c+top,tmpt+1])
        if b:
            top=b[-1]
            l=b[:len(b)-1]
            try:
                visited[(a+top,l,c)]
            except:
                visited[(a+top,l,c)]=tmpt+1
                queue.append([a+top,l,c,tmpt+1])
            try:
                visited[(a,l,c+top)]
            except:
                visited[(a,l,c+top)]=tmpt+1
                queue.append([a,l,c+top,tmpt+1])
        if c:
            top=c[-1]
            l=c[:len(c)-1]
            try:
                visited[(a,b+top,l)]
            except:
                visited[(a,b+top,l)]=tmpt+1
                queue.append([a,b+top,l,tmpt+1])
            try:
                visited[(a+top,b,l)]
            except:
                visited[(a+top,b,l)]=tmpt+1
                queue.append([a+top,b,l,tmpt+1])

bfs(*arr)

print(visited[last])



'''
for i in range(3):
    if len(arr[i])!=1:
        nowsize,stick=arr[i].split()
        size[i]=int(nowsize)
        arr[i]=list(stick)+[chr(65+i)*2]*(10-size[i])
    else:
        arr[i]=[chr(65+i)*2 for _ in range(10)]



def bfs(stick_a,stick_b,stick_c):
    queue=deque([stick_a,stick_b,stick_c])
    print(queue)
    print(sorted(queue))
'''
    
