numbers_of_c = int(input())
commands = int(input())


map_ = {}
for _ in range(commands):
    node_a, node_b = list(map(int,input().split()))
    if node_a not in map_:
        map_[node_a] =[]
    if node_b not in map_:
        map_[node_b] =[]

    map_[node_a].append(node_b)
    map_[node_b].append(node_a)

visited= [False for _ in range(numbers_of_c +1)]
visited[0] =True

q= []
q.append(1)
visited[1]=True

while q:
    go = q.pop()
    to = map_[go]
    for t in to:
        if visited[t] == False:
            visited[t]=True
            q.append(t)

print(sum(visited)-2)
