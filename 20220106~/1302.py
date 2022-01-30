from collections import defaultdict

v=defaultdict(int)
for i in range(int(input())):
    v[input()]+=1

print(sorted([(-w,c) for c,w in v.items()])[0][1])
