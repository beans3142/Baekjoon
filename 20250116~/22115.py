p=[0]*7**6
n,k=map(int,input().split())
if k:
    for i in map(int,input().split()):
        p[i]=1
        for j in range(k+1,0,-1):
            if p[j]:
                p[j+i]=min(p[j+i],p[j]+1) if p[j+i] else p[j]+1
    print(p[k] if p[k] else -1)
else:
    print(0)
