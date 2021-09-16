import sys
input=sys.stdin.readline

n,m=map(int,input().split())

never_seen=set()
never_heard=set()

for i in range(n+m):
    name=input().rstrip()
    if i < n:
        never_heard.add(name)
    else:
        never_seen.add(name)

never=sorted(never_seen.intersection(never_heard))
print(len(never))
for i in never:
    print(i)
    
