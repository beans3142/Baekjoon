from random import *

for i in range(10):
    n=randint(3,8)
    m=randint(1000,1000000)
    left=253
    arr=[[chr(65+i)] for i in range(n)]

    print(n,m)

    for i in range(n+1):
        get=randint(0,left)
        left-=get
        if i==n:
            continue
        arr[i].append(get)

    for i in range(n+1):
        get=randint(0,m)
        m-=get
        if i==n:
            continue
        arr[i].append(get)

    for i in arr:
        print(*i)
    print()
    print()
