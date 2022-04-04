import sys
input=sys.stdin.readline
n=int(input())
group={}
p=1
pl=[]
total=0
for i in range(n):
    sample=int(input())
    total+=sample
    if sample not in group:
        group[sample]=1
    else:
        group[sample]+=1
        if group[sample] > p:
            pl=[]
            p=group[sample]
    if group[sample]==p:
        pl.append(sample)
    if len(pl)>2:
        pl.remove(max(pl))

total=round(total/n)
n=n//2+1

for i in sorted(group):
    n-=group[i]
    if n<=0:
        break

print(total) #산술평균
print(i) #중앙값
print(max(pl)) # 최빈값
print(max(group)-min(group)) #범위
