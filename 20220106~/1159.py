from sys import stdin
input=stdin.readline

n=int(input())
firstname={chr(97+i):0 for i in range(26)}
ans=[]

for i in range(n):
    name=input().rstrip()[0]
    firstname[name]+=1
    if firstname[name]>4:
        ans.append(name)

able=''.join(sorted(set(ans)))
print(able if able else 'PREDAJA')
