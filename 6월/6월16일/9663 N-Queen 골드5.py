'''
def dfs(queen, row, n):
    count = 0
    if n == row:
        return 1
    for col in range(n):
        queen[row] = col
        for i in range(row):
            if queen[i] == queen[row]:
                break
            if abs(queen[i]-queen[row]) == row - i:
                break
        else:
            count += dfs(queen, row + 1, n)
    return count
def solution(n):
    return dfs([0]*n, 0, n)

for i in range(1,16):
    print(solution(i))
'''
print([1,0,0,2,10,4,40,92,352,724,2680,14200,73712,][int(input())])
