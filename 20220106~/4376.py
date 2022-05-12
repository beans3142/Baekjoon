from sys import stdin
input=stdin.readline

def dfs(x):
    
    if vi[x]:
        return False

    vi[x]=1
    
    for i in able[x]:
        if rev[i]==-1 or dfs(rev[i]):
            rev[i]=x
            return True
        
    return False

def getdist(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)

while True:
    try:
        n,m,s,v=map(int,input().split())

        mouse=[]
        hole=[]

        for i in range(n):
            mouse.append(list(map(lambda x:int(float(x)*1000),input().split())))

        for j in range(m):
            hole.append(list(map(lambda x:int(float(x)*1000),input().split())))

        able=[[] for i in range(n)]

        for i in range(n):
            for j in range(m):
                if getdist(*mouse[i],*hole[j])<=(s*v*1000)**2:
                    able[i].append(j)

        rev=[-1]*(m)
        cnt=0
        for i in range(n):
            vi=[0]*m
            if dfs(i):
                cnt+=1

        print(n-cnt)
    except:
        break
