from sys import stdin
input=stdin.readline

def mk(left):
    global no
    if left==0:
        no+=1
        if no==k:
            print(*arr,sep='+')
            exit()
        return
    if left>=1:
        arr.append(1)
        mk(left-1)
        arr.pop()
    if left>=2:
        arr.append(2)
        mk(left-2)
        arr.pop()
    if left>=3:
        arr.append(3)
        mk(left-3)
        arr.pop()
    

no=0
n,k=map(int,input().split())
arr=[]
mk(n)
print(-1)
