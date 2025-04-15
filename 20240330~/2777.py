from sys import stdin
input=stdin.readline
for _ in range(int(input())):
    n=int(input())
    if n==1:
        print(1)
        continue
    le=0
    while n>1:
        div=False
        for i in range(9,1,-1):
            if n%i==0:
                n//=i
                div=True
                le+=1
                break
        if not div:
            break
    if n>9:
        print(-1)
    else:
        print(le)
