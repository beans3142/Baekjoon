from sys import stdin
from itertools import permutations
input=stdin.readline

s1,s2,s3=map(list,input().split())

s=set(s1+s2+s3)

def stoi(st):
    intg=0
    for i in st:
        intg*=10
        intg+=case[i]
    return intg

case={i:0 for i in s}

if len(s)>10:
    print('NO')
    exit()

for i in permutations(range(10),len(s)):
    for idx,j in enumerate(case):
        case[j]=i[idx]

    n1=stoi(s1)
    n2=stoi(s2)
    n3=stoi(s3)
    if n1+n2==n3:
        print('YES')
        exit()

print('NO')
