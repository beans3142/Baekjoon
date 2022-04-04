n=int(input())

tile=[0,1,3]

for i in range(3,n+1):
    tile.append(tile[i-1]+2*tile[i-2])

print(tile[n]%10007)
