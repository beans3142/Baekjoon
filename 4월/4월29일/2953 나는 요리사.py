#https://www.acmicpc.net/problem/2953

score={}
max_total=0
who=1
for i in range(1,6):
    total=sum(map(int,input().split()))
    score[i]=total
    if max_total<total:
        max_total=total
        who=i

print(who,max_total)
