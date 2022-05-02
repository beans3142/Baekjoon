from sys import stdin
input=stdin.readline

n=int(input())
idx=list(map(int,input().split()))
h=list(map(int,input().split()))
ans=0

for i in range(1,n):
    cangrow=idx[i]-idx[i-1]-1
    if cangrow==0:
        continue
    hdif=abs(h[i]-h[i-1])
    mnh=min(h[i],h[i-1])
    mxh=max(h[i],h[i-1])
    if cangrow+1<hdif:
        print(0)
        exit()
    leftdist=cangrow-hdif
    if leftdist>1:
        ans=max(ans,mxh+(leftdist+1)//2)
    else:
        ans=max(ans,mxh-1)

print(ans)


'''
2
1 6
1 2

res=1 2 3 4 3 2
hdif=1
cangrow=4

ans=4

2
1 9
1 2

res = 1 2 3 4 5 4 3 2 2

ans=5

2
1 3
1 4

res 1 X 4

ans=0
불가능하므로

'''
