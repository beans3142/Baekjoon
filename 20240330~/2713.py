from sys import stdin
input=stdin.readline

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def makecircle(r,c,order):
    arr=[[-1]*c for i in range(r)]
    x=0
    y=0
    idx=0
    loc=0
    for i in range(r):
        for j in range(c):
            arr[y][x]=order[loc] if loc<len(order) else '0'
            loc+=1
            nx=x+dx[idx]
            ny=y+dy[idx]
            if not(-1<nx<c and -1<ny<r) or arr[ny][nx]!=-1:
                idx=(idx+1)%4
            x=x+dx[idx]
            y=y+dy[idx]
    ans=''.join([arr[i][j] for i in range(r) for j in range(c)])
    return ans

for _ in range(int(input())):
    inp=list(input())
    inp[-1]=' '
    r='';c=''
    while inp[0]!=' ':
        r+=inp.pop(0)
    inp.pop(0)
    while inp[0]!=' ':
        c+=inp.pop(0)
    inp.pop(0)
    r=int(r);c=int(c)
    order=''.join([bin(ord(i)-32)[3:] if i!= ' ' else '00000' for i in inp])
    print(makecircle(r,c,order))
