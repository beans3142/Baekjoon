from sys import stdin
from collections import defaultdict
input=stdin.readline

def find(tar):
    if par[tar]=='':
        par[tar]=tar
        rev[tar]+=1
    if tar==par[tar]:
        return tar
    par[tar]=find(par[tar])
    return par[tar]

for _ in range(int(input())):
    c=int(input())
    par=defaultdict(str)
    rev=defaultdict(int)
    for i in range(c):
        cnt=0
        a,b=input().rstrip().split()
        a=find(a)
        b=find(b)
        tg=min(a,b)
        if a<b:
            par[b]=a
            tg=a
            rev[a]+=rev[b]
        elif b<a:
            par[a]=b
            tg=b
            rev[b]+=rev[a]
        print(rev[tg])

'''

1
4
a b
b c
c a
b a

correct

2
3
3
3

/////

1
7
a b
b c
c a
d e
e d
d e
a b

correct

2
3
3
2
2
2
3
'''
