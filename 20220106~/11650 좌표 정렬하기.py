import sys
input=sys.stdin.readline
n=int(input())

xy=[list(map(int,input().split())) for i in range(n)]
sorted_xy={}

for dot in xy:
    x=dot[1]
    y=dot[0]
    if x not in sorted_xy:
        sorted_xy[x]=[y]
    else:
        sorted_xy[x].append(y)

for x in sorted(sorted_xy):
    for y in sorted(sorted_xy[x]):
        print(y,x)
