N, M = map(int,input().split())

maps = [[0 for _ in range(N)]for _ in range(N)]

for i in range(M):
    first, late = map(int,input().split())
    maps[first-1][late-1]=1
        #graph[first-1].append(late-1)
for k in range(N):
    for i in range(N):
        for j in range(N):
            if maps[i][k] and maps[k][j]:
                maps[i][j] = 1
questions = list()
for _ in range(int(input())):
    a, b= map(int,input().split())
    questions.append((a-1,b-1))
    #answer = solution(graph,questions)
for i in questions:
    a,b = i[0],i[1]
    if maps[a][b] == 1:
        print(-1)
    elif maps[b][a] == 1:
        print(1)
    else:
        print(0)
