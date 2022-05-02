def go(t):
    if t == len(ans):
        for i in range(9): print(*D[i])
        exit(0)
    x, y = ans[t][0], ans[t][1]
    for i in range(1, 10):
        if R[x][i] == C[y][i] == S[3 * (x // 3) + y // 3][i] == 0:
            R[x][i], C[y][i], S[3 * (x // 3) + y // 3][i], D[x][y] = 1, 1, 1, i
            go(t + 1)
            R[x][i], C[y][i], S[3 * (x // 3) + y // 3][i], D[x][y] = 0, 0, 0, 0


D = [[*map(int, list(input()))] for _ in range(9)]
C = [[0] * 10 for _ in range(9)]
R = [[0] * 10 for _ in range(9)]
S = [[0] * 10 for _ in range(9)]
ans = []
for i in range(9):
    for j in range(9):
        C[j][D[i][j]] += 1
        R[i][D[i][j]] += 1
        S[3 * (i // 3) + j // 3][D[i][j]] += 1
        if D[i][j] == 0: ans.append([i, j])
go(0)
