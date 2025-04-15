from sys import stdin,setrecursionlimit
setrecursionlimit(100000)
input=stdin.readline

def find(loc):
    r,c=loc
    if par[r][c]==(r,c):
        return loc
    par[r][c]=find(par[r][c])
    return par[r][c]

def union(a,b):
    pa=find(a)
    pb=find(b)
    if pa<pb:
        par[pb[1]][pb[0]]=pa
    else:
        par[pa[1]][pa[0]]=pb

n,m=map(int,input().split())
arr=[input().rstrip() for i in range(n)]
par=[[(r,c) for c in range(m)] for r  in range(n)]
dri={"D":[1,0],"R":[0,1],"U":[-1,0],"L":[0,-1]}

for r in range(n):
    for c in range(m):
        dr,dc=dri[arr[r][c]]
        nc=c+dc
        nr=r+dr
        union((r,c),(nr,nc))
        for x in par:
            print(x)
        print()
        
se=set()
for i in range(n):
    for j in range(m):
        se.add(find((j,i)))


print(len(se))
        


