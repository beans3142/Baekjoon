a=list(map(int,input().split()))
l=list(range(1,9))
if a[0]==1:
    if a==l:
        print('ascending')
        exit()
elif a[7]==1:
    if a==list(reversed(l)):
        print('descending')
        exit()
print('mixed')
