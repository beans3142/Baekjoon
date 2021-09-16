import sys
input=sys.stdin.readline

n=int(input())
house=[[0] for i in range(n)]

for i in range(n):
    house[i]=list(map(int,input().split()))
    if i > 0:
        house[i][0]+=min(house[i-1][1],house[i-1][2])
        house[i][1]+=min(house[i-1][2],house[i-1][0])
        house[i][2]+=min(house[i-1][1],house[i-1][0])

print(min(house[i]))
