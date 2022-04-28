from sys import stdin
input=stdin.readline

def bt(arr):
    if len(arr)==n:
        case.append(arr)
        return
    bt(arr+[-1])
    bt(arr+[1])
    

n=int(input())
beads=sorted(map(int,input().split()))
t=int(input())
case=[]
bt([])
total=0

for i in case:
    lidx=0
    ridx=n-1
    cnt=0
    lefttime=t
    nowbeads=beads[:]
    while True:
        dist=float('inf')
        #print(nowbeads,i)
        while lidx<n and i[lidx]==-1:
            lidx+=1

        while ridx>-1 and i[ridx]==1:
            ridx-=1

        if lidx>=ridx:
            break

        for j in range(lidx+1,ridx+1):
            if i[j-1]==1 and i[j]==-1:
                dist=min(dist,(abs(nowbeads[j]-nowbeads[j-1]))/2)
        #print(lidx,ridx,dist,nowbeads,i)
        if dist>lefttime:
            break

        for j in range(lidx,ridx+1):
            nowbeads[j]+=dist*i[j]

        for j in range(lidx+1,ridx+1):
            if nowbeads[j-1]==nowbeads[j]:
                if i[j-1]==-1:
                    i[j-1]=1
                    i[j]=-1
                else:
                    i[j-1]=-1
                    i[j]=1
                cnt+=1

        lefttime-=dist

    total+=cnt

print(total/2**n)
        
            
