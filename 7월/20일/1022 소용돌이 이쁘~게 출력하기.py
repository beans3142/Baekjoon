from math import log
r1,c1,r2,c2=map(int,input().split())

mx_len=max(abs(r1),abs(r2),abs(c1),abs(c2))
storm=[[0 for i in range(mx_len*2+1)]for j in range(mx_len*2+1)]
x=y=mx_len

storm[y][x]=1
idx=2
for n in range(mx_len+1):
    repeat=[(2*n-1),(2*n),(2*n),(2*n+1)]
    pattern=[[0,1],[-1,0],[0,-1],[1,0]]
    try:
        for redo,go in enumerate(pattern):
            for banbok in range(repeat[redo]):
                x+=go[0]
                y+=go[1]
                storm[~y][x]=idx
                idx+=1
    except:
        idx-=1
        break
r1+=mx_len
r2+=mx_len
c1+=mx_len
c2+=mx_len
biggest_num_len=int(max(log(storm[r1][c1],10),log(storm[r1][c2],10),\
                    log(storm[r2][c1],10),log(storm[r2][c2],10)))

for i in range(r1,r2+1,1):
    for j in range(c1,c2+1,1):
        print(' '*(biggest_num_len-int(log(storm[i][j],10))),storm[i][j],end=' ',sep='')
    print()
