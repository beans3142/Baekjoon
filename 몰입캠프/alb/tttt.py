from collections import defaultdict

numbers_of_nodes , root_node = list(map(int , input().split() ))
map_ = defaultdict(dict)
for _ in range(numbers_of_nodes-1):
    up, down  = list( map(int , input().split() ))
    if up not in map_:
        map_[up] = {'up':[],'down':[]}
    if down not in map_:
        map_[down] = {'up':[],'down':[]}
    map_[down]['up'].append(up)
    map_[up]['down'].append(down)

max_ =0
def dfs(count , x, q):
    global max_
    if map_[x]['down']==[]:
        max_ = max(max_,count)
        return
    while q:
        go = q.pop()
        dfs(count+1, go, map_[go]['down']+map_[go]['up'])

dfs(0,root_node,[0])
print(max_-1)
