from sys import stdin
input=stdin.readline

dx=[1,-1,0,0]
dy=[0,0,1,-1]

typ=[[],[[0],[1],[2],[3]],[(0,1),(2,3)],[[0,3],[0,2],[1,2],[1,3]],\
     [(0,1,2),(1,2,3),(0,1,3),(0,2,3)],[[0,1,2,3]]]


def bt(idx):
    global ans
    if idx==len(loc):
        '''
        for i in see:
            print(i)
        print()'''
        ans=min(ans,countsafe())
        return

    x,y,t=loc[idx]
    
    for i in typ[t]:
        for j in i:
            fill(x,y,j,1)
        bt(idx+1)
        for j in i:
            fill(x,y,j,-1)

def fill(x,y,face,val):
    try:
        while True:
            x+=dx[face]
            y+=dy[face]
            if y<0 or x<0:
                return
            if matrix[y][x]==6:
                return
            see[y][x]+=val
    except:
        pass

def countsafe():
    cnt=0
    for i in range(n):
        for j in range(m):
            if see[i][j]==0 and matrix[i][j]==0:
                cnt+=1
    return cnt
    
        
ans=10e9
n,m=map(int,input().split())
matrix=[list(map(int,input().split())) for i in range(n)]
see=[[0]*m for i in range(n)]

loc=[]

for i in range(n):
    for j in range(m):
        if matrix[i][j]==6:
            see[i][j]=-1
        elif matrix[i][j]!=0:
            loc.append([j,i,matrix[i][j]])


bt(0)

print(ans)
