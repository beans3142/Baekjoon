t=int(input())
a=b=c=0
if t%10==0:
    a=t//300
    t%=300
    if t!=0:
        b=t//60
        t%=60
        if t!=0:
            c=t//10
    print(a,b,c)
else:
    print(-1)

#https://www.acmicpc.net/problem/10162
