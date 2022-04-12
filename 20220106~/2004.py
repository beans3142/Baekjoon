def cn(n,num):
    cnt=0
    while n:
        cnt+=(n//num)
        n//=num
    return cnt
n,m=map(int,input().split())
print(min(cn(n,5)-cn(m,5)-cn(n-m,5),cn(n,2)-cn(m,2)-cn(n-m,2)))
