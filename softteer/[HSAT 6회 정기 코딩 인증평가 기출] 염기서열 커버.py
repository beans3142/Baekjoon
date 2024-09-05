from sys import stdin
from collections import defaultdict
input=stdin.readline


def check(s1,s2):
    s3=list(s1)
    for i in range(m):
        if s1[i]!=s2[i]:
            if s1[i]!='.' and s2[i]!='.':
                return False
            if s1[i]=='.':
                s3[i]=s2[i]
    
    return tuple(s3)
            
def makekey(s):
    key=0
    for i in range(n):
        if check(s,arr[i]):
            key|=1<<i
    return key

n,m=map(int,input().split())
arr=[input().rstrip() for i in range(n)]
keySet=set()

cho=[(arr[i],1<<i) for i in range(n)]

for i in range(n):
    keySet.add(1<<i)

while True:
    ncho=[]
    for i in range(len(cho)):
        for j in range(i+1,len(cho)):
            s=check(cho[i][0],cho[j][0])
            if s:
                key=cho[i][-1]|cho[j][-1]
                ncho.append((s,key))
                keySet.add(key)
                
    if not ncho:
        break
    cho=list(set(ncho))


nkey=set(keySet)
cnt=1
while True:
    if 2**n-1 in nkey:
        break
    nxt=set()
    for i in nkey:
        for j in keySet:
            if i!=j and i|j not in nkey:
                nxt.add(i|j)
    nkey=set(nxt)
    cnt+=1

print(cnt)
