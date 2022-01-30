k,n=map(int,input().split())

print((k*n)//(n-1)+bool((k*n)%(n-1)) if n!=1 else -1)
