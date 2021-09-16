l=int(input())
dalpaeng=[[1]*l for i in range(l)]
x=y=l//2
idx=2
for n in range(l):
    repeat=[(2*n-1),(2*n),(2*n),(2*n+1)]
    pattern=[[1,0],[0,-1],[-1,0],[0,1]]
    try:
        for redo,go in enumerate(pattern):
            for banbok in range(repeat[redo]):
                x+=go[0]
                y+=go[1]
                dalpaeng[~y][x]=idx
                idx+=1
    except:
        break

f=int(input())

for i in range(l):
    for j in range(l):
        if dalpaeng[i][j]==f:
            ans=[i+1,j+1]
        print(dalpaeng[i][j],end=' ')
    print()

print(*ans)
