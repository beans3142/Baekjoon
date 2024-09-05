from sys import stdin
input=stdin.readline

def getdist(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def mul(y1,y2):
    if y1<y2:
        return 3
    elif y1==y2:
        return 2
    else:
        return 1

n,m=map(int,input().split())
arrx=list(map(int,input().split()))
arry=list(map(int,input().split()))


presum=[0,0]
pd=[0,0]

for i in range(1,n):
    presum.append(presum[-1]+getdist(arrx[i],arry[i],arrx[i-1],arry[i-1])*mul(arry[i-1],arry[i]))

arrx=arrx[::-1]
arry=arry[::-1]

for i in range(1,n):
    pd.append(pd[-1]+getdist(arrx[i],arry[i],arrx[i-1],arry[i-1])*(mul(arry[i-1],arry[i])))

for _ in range(m):
    a,b=map(int,input().split())
    if a<b:
        print(presum[b]-presum[a])
    else:
        b=n-b+1
        a=n-a+1
        print(pd[b]-pd[a])