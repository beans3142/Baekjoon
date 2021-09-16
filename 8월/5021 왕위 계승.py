from sys import stdin
from collections import defaultdict
input=stdin.readline
n,m=map(int,input().split())
king=input().rstrip()
family=defaultdict(list)
blood=defaultdict(int)
blood[king]=1

for i in range(n):
    son,par,ent=input().rstrip().split()
    family[son].extend([par,ent])
    family[par]
    family[ent]
    blood[son]=0

while family:
    for i in family:
        if not family[i]:
            for j in family:
                if i in family[j]:
                    family[j].remove(i)
                    blood[j]+=blood[i]/2
            del family[i]
            break

wanna_be_the_king=[]
for i in range(m):
    person=input().rstrip()
    wanna_be_the_king.append([blood[person],person])

print(sorted(wanna_be_the_king)[-1][1])
