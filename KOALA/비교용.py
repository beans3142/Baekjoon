def rotate2(key):
    M = len(key)
    rotatedKey = [[0] * M for _ in range(M)]
    for row in range(M):
        for col in range(M):
            rotatedKey[row][col] = key[M - col - 1][row]
    return rotatedKey
 
 
def createExtendedMatrix(key, lock):
    M, N = len(key), len(lock)
    extended = [[0] * (M + 2 * (N - 1)) for _ in range(M + 2 * (N - 1))]
    for row in range(M - 1, M + N - 1):
        for col in range(M - 1, M + N - 1):
            extended[row][col] = lock[row - M + 1][col - M + 1]
    return extended
 
 
def search(key, lock):
    M, N = len(key), len(lock)
    searchResult = False
    for startRow in range(M + N - 1):
        for startCol in range(M + N - 1):
            extended = createExtendedMatrix(key, lock)
            for row in range(M):
                for col in range(M):
                    extended[startRow + row][startCol + col] += key[row][col]
            searchResult = checkKeyMatchesLock(M, N, extended)
            if searchResult:
                return True
 
 
def checkKeyMatchesLock(M, N, extended):
    for row in range(M - 1, M + N - 1):
        for col in range(M - 1, M + N - 1):
            if extended[row][col] != 1:
                return False
    return True
 
 
def solution(key, lock):
    for _ in range(4):
        key = rotate2(key)
        #print(key)
        searchResult = search(key, lock)
        if searchResult:
            return True
    return False
