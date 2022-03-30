from sys import stdin
from bisect import bisect_right
input=stdin.readline

n,q=map(int,input().split())
arr=[*map(lambda x:-int(x),input().split())]
for i in range(q):
    y,x=map(int,input().split())
    x-=1
    if x<n and y<=-arr[x]:
        garo=bisect_right(arr,-y)-x
        sero=-arr[x]-y
        print(garo+sero)
    else:
        print(0)

'''
3 5
3 2 1
1 1
1 2
1 3
2 2
3 1

>>
5
3
1
1
1

3 5
1 1 1
1 1
40102 1
3 1

>>
3
0
1

4 4
4 4 2 1

'''
