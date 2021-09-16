from sys import stdin,maxsize
from itertools import permutations
input=stdin.readline

n=int(input())
jido=[list(input().rstrip()) for i in range(n)]
job={'Assassin':[],'Healer':[],'Mage':[],'Tanker':[],'Home':[],'End':[]}
reverse_job={'J':'Assassin','C':'Healer','B':'Mage','W':'Tanker','H':'Home','#':'End'}
mn=maxsize
ans=''

for i in range(n):
    for j in range(n):
        if jido[i][j] !='X':
            job[reverse_job[jido[i][j]]].append((j,i))


jobs=['Assassin','Healer','Mage','Tanker']
start=job['Home'][0]
end=job['End'][0]
for i in jobs:
    case=list(permutations(job[i],3))
    for j in case:
        total_dist=0
        total_dist+=abs(start[0]-j[0][0])+abs(start[1]-j[0][1])
        total_dist+=abs(end[0]-j[2][0])+abs(end[1]-j[2][1])
        for k in range(1,3):
            total_dist+=abs(j[k-1][0]-j[k][0])+abs(j[k-1][1]-j[k][1])
        if total_dist<mn:
            ans=i
            mn=total_dist
        
print(ans)
