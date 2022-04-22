from sys import stdin
from copy import deepcopy
from itertools import permutations
input=stdin.readline

def check(arr):
    for i in arr:
        buy(i)

def buy(i):
    global money
    money+=price[i]
    for j in sale[i]:
        price[j[0]]=max(price[j[0]]-j[1],1)

n=int(input())
Price=list(map(int,input().split()))
sale=[[] for i in range(n)]

for i in range(n):
    pi=int(input())
    for j in range(pi):
        item,discount=map(int,input().split())
        sale[i].append([item-1,discount])

ans=10e9
for i in permutations([i for i in range(n)],n):
    money=0
    price=deepcopy(Price)
    check(i)
    ans=min(money,ans)

print(ans)
