from time import *

n=1000
arr=[i for i in range(n)]

now=time()
for i in range(n): 
    print(i,arr[i])
t1=time()-now

now=time()
for idx,i in enumerate(arr):
    print(idx,i)
t2=time()-now

print(t1,t2)

now=time()
for i in range(n):
    print(arr[i])
t1=time()-now()
