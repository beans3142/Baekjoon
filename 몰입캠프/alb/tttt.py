from collections import defaultdict

numbers_of_nodes , node_a ,node_b = list(map(int , input().split() ))
map_ = defaultdict(dict)
for _ in range(numbers_of_nodes-1):
    up, down  = list( map(int , input().split() ))
    if up not in map_:
        map_[up] = {'up':-1}
    if down not in map_:
        map_[down] = {'up':-1}
    map_[down]['up'] = up

while map_[node_a]['up'] !=  map_[node_b]['up']:
    up_a = map_[node_a]['up']
    up_b = map_[node_b]['up']
    
    if up_a == up_b:
        print(up_a)
        break
    
    if map_[up_a]['up'] == up_b:
        print(up_b)
        break
    
    if map_[up_b]['up'] == up_a:
        print(up_a)
        break
    
    node_a = up_a
    node_b = up_b
