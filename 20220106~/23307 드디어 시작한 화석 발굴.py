from sys import stdin
input=stdin.readline

n=int(input())
v=[[0 for i in range(n)] for j in range(n)]
arr=[input().rstrip() for i in range(n)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
name1={0:'D',1:'U',2:'R',3:'L'}
name2={0:'U',1:'D',2:'L',3:'R'}
rev={'U':'D','D':'U','R':'L','L':'R'}
result=[]

def check(x,y):
    ans=''
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if arr[ny][nx]=='#':
            ans+=name1[i]
            ny+=dy[i]
            nx+=dx[i]
            x=nx
            y=ny
            break

    for i in range(4):
        try:
            nx=x+dx[i]
            ny=y+dy[i]
            if rev[name2[i]]!=ans and ans!=name2[i] and arr[ny][nx]=='#':
                ans+=name2[i]
                return ans
        except:
            pass

for i in range(n):
    for j in range(n):
        if v[i][j]==0:
            side=0
            if arr[i][j]=='#':
                try:
                    while arr[i+side][j]=='#' or arr[i][j+side]=='#':
                        side+=1
                except:
                    pass
                side-=1
                mx=j+side//2
                my=i+side//2
                result.append((my+1,mx+1,side+1,check(mx,my)))
                

            for y in range(side+1):
                for x in range(side+1):
                    v[i+y][j+x]=1

for i in sorted(result):
    print(*i)
            
