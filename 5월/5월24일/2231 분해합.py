n=int(input())

for i in range(1,n+1):
    x=i
    for j in str(i):
       x+=int(j)
    if x==n:
        print(i)
        exit()

print(0)
