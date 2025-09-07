from collections import*
a,b,n,m=map(int,input().split())
q=deque([n])
v=[1e9]*100001
v[n]=0
while q:
    w=q.popleft()
    for i in [1,-1,a,b,-a,-b,w*a-w,w*b-w]:
        W=w+i
        V=v[w]+1
        if 0<=W<=100000 and v[W]>V:
            v[W]=V
            q.append(W)
print(v[m])
