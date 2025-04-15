from copy import deepcopy

def solve():
    arr = [list(map(int, input().split())) for i in range(6)]
    ans = checkcase(arr)

    for i in range(6):
        for k in range(1, 10):
            for ii in range(6):
                for kk in range(1, 10):
                    arr[ii][5 - ii]+=kk
                    arr[i][i]+=k
                    ans = max(ans, checkcase(arr))
                    arr[ii][5 - ii]-=kk
                    arr[i][i]-=k

    return ans

def checkcase(arr):
    return checkrow(0, arr)

def checkrow(row, arr):
    res = 0
    if row == 6:
        return checkcol(arr)
    for i in range(6):
        dif = 9 - arr[row][i]%10
        for j in range(6):
            arr[row][j] += dif
        res = max(res, checkrow(row + 1, arr))
        for j in range(6):
            arr[row][j] -= dif
    return res

def checkcol(arr):
    res = 0
    for col in range(6):
        maxline = 0
        for row in range(6):
            line=0
            dif=9-arr[row][col]%10
            for k in range(6):
                line+=(arr[k][col]+dif)%10
            maxline=max(line,maxline)
        res+=maxline
    return res

answer = solve()
print(answer)
