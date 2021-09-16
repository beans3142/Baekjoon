from sys import stdin
from collections import deque

# 변의 길이 입력받고 그 배열을 만들고 입력받은 값중 가장 큰 값을 저장하는 부분
n=int(input())
mx=0
board=[]

for i in range(n):
    board.append(list(map(int,input().split())))
    mx=max(mx,max(board[-1]))

# 왼,오,위,아래로 합치는 함수들 정의

# -함수들의 기본 형태-
# 0 이 아닌 값만 모으기
# 모은 값들을 특정 방향으로 합치기
# 합쳐진/합쳐지지 않은 값들을 새 배열에 알맞은 순서로 넣어줌.

def l(narr):
    global mx
    to_check=[[]for i in range(n)]
    for i in range(n):
        for j in range(n):
            if narr[i][j]!=0:
                to_check[i].append(narr[i][j])
                #narr[i][j]=0
    arr=[[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        if len(to_check[i])==1:
            arr[i][0]=to_check[i][0]
        elif len(to_check[i])>1:
            check_idx=1
            fill_idx=0
            while check_idx<len(to_check[i]):
                #print(arr[i],to_check,check_idx,fill_idx)
                if to_check[i][check_idx-1]==to_check[i][check_idx]:
                    arr[i][fill_idx]=2*to_check[i][check_idx-1]
                    mx=max(arr[i][fill_idx],mx)
                    fill_idx+=1
                    check_idx+=2
                else:
                    arr[i][fill_idx]=to_check[i][check_idx-1]
                    fill_idx+=1
                    check_idx+=1
            if check_idx==len(to_check[i]):
                arr[i][fill_idx]=to_check[i][-1]
    return arr

def r(narr):
    global mx
    to_check=[[]for i in range(n)]
    for i in range(n):
        for j in range(n):
            if narr[i][j]!=0:
                to_check[i].append(narr[i][j])
                #narr[i][j]=0
    arr=[[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        if len(to_check[i])==1:
            arr[i][-1]=to_check[i][0]
        elif len(to_check[i])>1:
            check_idx=1
            fill_idx=0
            while check_idx<len(to_check[i]):
                #print(arr[i],to_check,check_idx,fill_idx)
                if to_check[i][~check_idx]==to_check[i][~check_idx+1]:
                    arr[i][~fill_idx]=2*to_check[i][~check_idx+1]
                    mx=max(mx,arr[i][~fill_idx])
                    fill_idx+=1
                    check_idx+=2
                else:
                    arr[i][~fill_idx]=to_check[i][~check_idx+1]
                    fill_idx+=1
                    check_idx+=1
            if check_idx==len(to_check[i]):
                arr[i][~fill_idx]=to_check[i][0]
    return arr

def d(narr):
    global mx
    to_check=[[]for i in range(n)]
    for i in range(n):
        for j in range(n):
            if narr[j][i]!=0:
                to_check[i].append(narr[j][i])
                #narr[i][j]=0
    arr=[[0 for i in range(n)]for j in range(n)]

    for i in range(n):
        if len(to_check[i])==1:
            arr[-1][i]=to_check[i][0]
        elif len(to_check[i])>1:
            check_idx=1
            fill_idx=0
            while check_idx<len(to_check[i]):
                #print(arr[i],to_check,check_idx,fill_idx)
                if to_check[i][check_idx-1]==to_check[i][check_idx]:
                    arr[~fill_idx][i]=2*to_check[i][check_idx-1]
                    mx=max(mx,arr[~fill_idx][i])
                    fill_idx+=1
                    check_idx+=2
                else:
                    arr[~fill_idx][i]=to_check[i][check_idx-1]
                    fill_idx+=1
                    check_idx+=1
            if check_idx==len(to_check[i]):
                arr[~fill_idx][i]=to_check[i][-1]
    return arr

def u(narr):
    global mx
    to_check=[[]for i in range(n)]
    for i in range(n):
        for j in range(n):
            if narr[j][i]!=0:
                to_check[i].append(narr[j][i])
                #narr[i][j]=0
    arr=[[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        if len(to_check[i])==1:
            arr[0][i]=to_check[i][0]
        elif len(to_check[i])>1:
            check_idx=1
            fill_idx=0
            while check_idx<len(to_check[i]):
                #print(arr[i],to_check,check_idx,fill_idx)
                if to_check[i][~check_idx]==to_check[i][~check_idx+1]:
                    arr[fill_idx][i]=2*to_check[i][~check_idx+1]
                    mx=max(arr[fill_idx][i],mx)
                    fill_idx+=1
                    check_idx+=2
                else:
                    arr[fill_idx][i]=to_check[i][~check_idx+1]
                    fill_idx+=1
                    check_idx+=1
            if check_idx==len(to_check[i]):
                arr[fill_idx][i]=to_check[i][0]
    return arr
        
# bfs 진행

queue=deque([[board,0]])

while queue:
    matrix,tmpt=queue.popleft()
    if tmpt==5:
        break
    queue.append([u(matrix),tmpt+1])
    queue.append([l(matrix),tmpt+1])
    queue.append([r(matrix),tmpt+1])
    queue.append([d(matrix),tmpt+1])

print(mx)
