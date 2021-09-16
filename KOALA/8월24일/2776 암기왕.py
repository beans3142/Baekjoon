from collections import defaultdict
from sys import stdin

for i in range(int(input())):
    dic=defaultdict(int)
    int(input())
    for j in map(int,input().split()):
        dic[j]=1
    int(input())
    for j in map(int,input().split()):
        print(dic[j])
