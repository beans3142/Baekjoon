from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(3000)
from collections import deque,defaultdict
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
from math import *

for _ in range(int(input())):
    s=input().rstrip()
    acnt=0
    bcnt=0
    ans=0
    ss=sorted([i.count("A") for i in s.split('B')],reverse=True)
    for i in range(s.count("B")):
        ans+=ss[i]
    print(ans)

"BAAABA"
"CBABCA"

"BAAAAA"