s=''.join(input().split())
d={}
n=1
for i in range(10000):
    i=str(i)
    b=0
    if '0' in i:continue
    for j in range(4):
        if i[j:]+i[:j] in d: continue
        d[i[j:]+i[:j]]=n
        b=1
    if b:n+=1
print(d[s])