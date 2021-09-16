#https://www.acmicpc.net/problem/1034

n,m=map(int,input().split())
#lamps={}
lamps=[]
for i in range(0,n):
    a=input()
    lamps+=[[i for i in a if i=='1'].count('1')]
    #lamps[i+1]=[i for i in a if i=='1']

k=int(input())
lamps.sort()
on=0

while True:
    for i in range(0,len(lamps)):
        if lamps[i]<m:
            while k!=0 and lamps[i]<m:
                lamps[i]+=1
                k-=1
    break

print(lamps.count(m))
'''
while True:
    most_on=0
    for j,i in enumerate(list(lamps.values())[:]):
        
    print
    break
'''
