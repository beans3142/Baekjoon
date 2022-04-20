from sys import stdin
input=stdin.readline

n=int(input())
mxdp=[list(map(int,input().split()))]
mndp=mxdp[:]

for i in range(n-1):
    a,b,c=map(int,input().split())
    na,nb,nc=mxdp.pop()
    ma,mb,mc=mndp.pop()
    mxdp.append([a+max(na,nb),b+max(na,nb,nc),c+max(nb,nc)])
    mndp.append([a+min(ma,mb),b+min(ma,mb,mc),c+min(mb,mc)])

print(max(mxdp[0]),min(mndp[0]))
