from sys import stdin
from bisect import bisect_left
input=stdin.readline

n=int(input())
arr=sorted(map(int,input().split()))

qidx=0

for i in range(1,arr[-1]):
    if i<n:
        bidx=bisect_left(arr,i)
        qidx=i

print(qidx)

# 아니 이거 왜 안돼지 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
