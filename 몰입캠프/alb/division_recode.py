def div(left,n,s):
    global cnt
    if left==0:
        print(*s,sep='+')
        cnt+=1
        return
    for i in range(n,0,-1):
        if left>=i:
            div(left-i,i,s+[i])

n=int(input())
cnt=0
div(n,n-1,[])
print(cnt)
