from sys import stdin
input=stdin.readline

def bt(idx,cnt):
    if cnt==6:
        print(*ans)
        return
    for i in range(idx,n):
        ans[cnt]=arr[i]
        bt(i+1,cnt+1)
    

while True:
    try:
        n,*arr=map(int,input().split())
        ans=[0]*6
        bt(0,0)
        print()
    except:
        break
