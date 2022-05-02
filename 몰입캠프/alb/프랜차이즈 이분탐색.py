from sys import stdin
from bisect import *
input=stdin.readline

n,m=map(int,input().split())
arr=[list(map(int,list(input().rstrip()))) for i in range(n)]

