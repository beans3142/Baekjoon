from sys import *
input=stdin.readline
inf=maxsize

while True:
    n=int(input())
    if n==0:
        break
    l={i:idx for idx,i in enumerate(input().rstrip().split())}
    val=[[[inf,j] for j in l] for i in range(n)]
    for i in range(n-1):
        big,equal,mul,small=input().rstrip().split()
        mul=int(mul)
        val[l[big]][l[small]][0]=mul
        val[l[small]][l[big]][0]=1/mul
    
    '''
    for i in val:
        print(i)
    '''
    for i in range(n):
        val[i][i][0]=1
        for j in range(n):
            for k in range(n):
                n_val=val[j][i][0]*val[i][k][0]
                val[j][k][0]=min(val[j][k][0],n_val if n_val<0.5 else round(n_val,1))

    for i in val:
        if sorted(i)[0][0]==1:
            ans=[str(int(size))+unit for size,unit in sorted(i)]
            print(" = ".join(ans))
