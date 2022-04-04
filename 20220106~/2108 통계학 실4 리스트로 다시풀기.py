import sys
input=sys.stdin.readline

n=int(input())
l=sorted([int(input()) for i in range(n)])+[4001]

pl=[l[0]]
p=0
t=0

for i in range(n):
    if l[i]==l[i+1]:
        t+=1
    else:
        if t>p:
            pl=[]
            if l[i] not in pl:
                pl.append(l[i])
            p=t
        elif t==p:
            if l[i] not in pl:
                pl.append(l[i])
        t=0
        if len(pl)>2:
            pl.remove(max(pl))

print(round(sum(l[:-1])/n))
print(l[(len(l)-1)//2])
print(max(pl))
print(l[-2]-l[0])
