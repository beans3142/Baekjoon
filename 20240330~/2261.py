from sys import stdin
input=stdin.readline

def getdist(dot1,dot2):
    dx=dot1[0]-dot2[0]
    dy=dot1[1]-dot2[1]
    return dx**2+dy**2

def div_conq(s,e):
    print(s,e)
    if e-s<3:
        mndist=1e10
        for i in range(s,e):
            for j in range(i+1,e+1):
                mndist=min(mndist,getdist(arr[i],arr[j]))
        return mndist

    mid=(s+e)//2
    mndist=min(div_conq(s,mid),div_conq(mid+1,e))
    mdv=arr[mid]
    narr=[]

    for i in range(s,e+1):
        if (arr[i][0]-mdv[0])**2<mndist:
            narr.append(arr[i])

    narr.sort()
    le=len(narr)

    for i in range(le):
        for j in range(i+1,le):
            mndist=min(mndist,getdist(narr[i],arr[j]))

    return mndist

n=int(input())
arr=sorted([list(map(int,input().split())) for i in range(n)])

print(div_conq(0,n-1))