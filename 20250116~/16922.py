# n=int(input())
# d={}
# v=[1,5,10,50]
# def bt(op,dep,s):
#     if dep==n:
#         d[s]=1
#         return
#     for i in range(op):
#         bt(i+1,dep+1,s+v[i])
# bt(4,0,0)
# print(len(d))

from itertools import *
print(len(set(map(sum,combinations_with_replacement([1,5,10,50],int(input()))))))