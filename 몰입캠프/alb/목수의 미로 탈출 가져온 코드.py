from collections import deque
import sys
input = sys.stdin.readline

def main(N,M):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    # 0 : not visited   1 : visited by case 1    2 : visited by case 0,1(or, by 0 only)
    visited[0][0] = 2
    queue = deque([(N-1,0,0)])
    res=0
    while queue:
        L = len(queue)
        for _ in range(L):
            r,c,case = queue.popleft()
            if r == 0 and c == M-1:
                return res
            for new_r,new_c in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                if 0<=new_r<N and 0<=new_c<M:
                    if case == 0 and visited[new_r][new_c] != 2:
                        if arr[new_r][new_c] == 0:
                            queue.append((new_r,new_c,0))
                        else:
                            queue.append((new_r,new_c,1))
                        visited[new_r][new_c] = 2
                    else:
                        if arr[new_r][new_c] == 0 and visited[new_r][new_c] == 0:
                            queue.append((new_r,new_c,1))
                            visited[new_r][new_c] = 1
        res+=1

    return -1

N,M = [int(x) for x in input().split()]
arr = [list(map(int,input().split())) for _ in range(N)]
print(main(N,M))
