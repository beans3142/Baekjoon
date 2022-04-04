from sys import stdin
input=stdin.readline

n,m=map(int,input().split())
_class={i:[] for i in range(1,n+1)}
total_participant=0
while total_participant<500:
    try:
        ban,name=input().rstrip().split()
        ban=int(ban)
        if len(_class[ban])<m:
            _class[ban].append((len(name),name))
            total_participant+=1
    except:
        break

for i in range(1,n+1,2):
    for j in sorted(_class[i]):
        print(i,j[1])

for i in range(2,n+1,2):
    for j in sorted(_class[i]):
        print(i,j[1])
