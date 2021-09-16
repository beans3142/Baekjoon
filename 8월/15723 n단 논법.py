from sys import *
input=stdin.readline
inf=maxsize

n=int(input())
val=[[inf]*26 for i in range(26)]
for i in range(n):
    premise=input().rstrip()
    val[ord(premise[0])-97][ord(premise[-1])-97]=1

for i in range(26):
    val[i][i]=1
    for j in range(26):
        for k in range(26):
            val[j][k]=min(val[j][k],val[j][i]+val[i][k])

m=int(input())

for i in range(m):
    is_able=input().rstrip()
    ans=val[ord(is_able[0])-97][ord(is_able[-1])-97]
    if ans!=inf:
        print("T")
    else:
        print("F")
