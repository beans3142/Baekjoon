n=int(input())
for i in range(n-1):
    print(' '*(n-i-1)+'*'*(2*i+1))
print('*'*(2*n-1))
for i in range(n-1):
    print(' '*(i+1)+'*'*(2*n-2-2*i-1))
