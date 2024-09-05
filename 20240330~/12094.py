from sys import stdin, setrecursionlimit
import copy

input = stdin.readline
setrecursionlimit(10000)

# 입력과 초기화
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 이동 및 병합 함수
def move_and_merge(arr, direction):
    new_arr = [[0] * n for _ in range(n)]

    for i in range(n):
        line = []
        for j in range(n):
            if direction == 'L' and arr[i][j] != 0:
                line.append(arr[i][j])
            elif direction == 'R' and arr[i][n - 1 - j] != 0:
                line.append(arr[i][n - 1 - j])
            elif direction == 'U' and arr[j][i] != 0:
                line.append(arr[j][i])
            elif direction == 'D' and arr[n - 1 - j][i] != 0:
                line.append(arr[n - 1 - j][i])

        merged_line = merge(line)
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

def merge(line):
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
    return merged_line

# 최대 블록 값 계산
def max_block(arr):
    return max(max(row) for row in arr)

# DFS 진행
def dfs(board, depth, max_depth):
    global result
    if depth == max_depth:
        result = max(result, max_block(board))
        return

    for direction in ['L', 'R', 'U', 'D']:
        new_board = move_and_merge(board, direction)
        if new_board != board:  # 상태가 변하지 않으면 가지치기
            dfs(new_board, depth + 1, max_depth)

# 초기화
result = 0
max_depth = 10
dfs(board, 0, max_depth)
print(result)
