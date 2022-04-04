from sys import stdin
import heapq

input=stdin.readline

heap=[]
n=int(input())

for i in range(n):
    a=int(input())
    if a==0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap,(abs(a),a))
