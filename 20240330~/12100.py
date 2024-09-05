from sys import stdin
from collections import deque

input = stdin.readline

# 입력과 초기화
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 이동 및 병합 함수
def move_and_merge(arr, direction):
    new_arr = [[0] * n for _ in range(n)]

    for i in range(n):
        line = []
        if direction in ['L', 'R']:
            for j in range(n):
                if direction == 'L':
                    if arr[i][j] != 0:
                        line.append(arr[i][j])
                else:
                    if arr[i][n - 1 - j] != 0:
                        line.append(arr[i][n - 1 - j])
        else:
            for j in range(n):
                if direction == 'U':
                    if arr[j][i] != 0:
                        line.append(arr[j][i])
                else:
                    if arr[n - 1 - j][i] != 0:
                        line.append(arr[n - 1 - j][i])
        
        merged_line = []
        skip = False
        for k in range(len(line)):
            if skip:
                skip = False
                continue
            if k < len(line) - 1 and line[k] == line[k + 1]:
                merged_line.append(2 * line[k])
                skip = True
            else:
                merged_line.append(line[k])

        if direction in ['L', 'U']:
            for k in range(len(merged_line)):
                if direction == 'L':
                    new_arr[i][k] = merged_line[k]
                else:
                    new_arr[k][i] = merged_line[k]
        else:
            for k in range(len(merged_line)):
                if direction == 'R':
                    new_arr[i][n - 1 - k] = merged_line[k]
                else:
                    new_arr[n - 1 - k][i] = merged_line[k]
    
    return new_arr

# BFS 진행
def bfs():
    queue = deque([(board, 0)])
    max_value = max([max(board[i]) for i in range(len(board))])
    
    while queue:
        matrix, steps = queue.popleft()
        if steps == 5:
            continue

        for direction in ['L', 'R', 'U', 'D']:
            new_matrix = move_and_merge(matrix, direction)
            if new_matrix != matrix:  # 중복 방지를 위해 새로운 상태만 큐에 추가
                queue.append((new_matrix, steps + 1))
                max_value = max(max_value, max(map(max, new_matrix)))
    
    return max_value

print(bfs())
