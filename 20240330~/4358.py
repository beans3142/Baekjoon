from sys import stdin
from collections import defaultdict
input=stdin.readline

dd=defaultdict(int)
boonmo=0
while True:
    s=input().rstrip()
    if not s:
        break
    boonmo+=1
    dd[s]+=1


for i in sorted(dd):
    print(f'{i} {round(100*dd[i]/boonmo,4):.4f}')
    
