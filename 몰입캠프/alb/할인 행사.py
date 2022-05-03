from collections import defaultdict

n=int(input())
dd=defaultdict(set)
for i in range(n):
    name,cnt,*items=input().split()
    dd[name]
    for item in items:
        dd[name].add(item)

ans=sorted([(len(bought),name) for name,bought in dd.items()],reverse=True)
print(ans[0][-1])
