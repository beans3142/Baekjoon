n,m=map(int,input().split())
print(n,m)
arr=[]
for i in range(n):
    arr+=[input()]


for i in arr[::-1]:
    for j in i:
        print('0' if j=='1' else '1',end=' ')
    print()
