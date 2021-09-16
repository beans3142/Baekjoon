from sys import stdin
input=stdin.readline
n,k=map(int,input().split())

matrix=[list(map(int,input().split())) for i in range(n)]
ans=10**15
vi=[0]*n
total_dist=0
'''
for i in range(n):
    matrix[i][i]=0
    for j in range(n):
        for k in range(n):
            matrix[j][k]=min(matrix[j][k],matrix[j][i]+matrix[i][k])


            '''

def bt(now,vis_cnt):
    global total_dist
    for i in range(n):
        if vi[i]==0:
            vi[i]=1
            total_dist+=matrix[now][i]
            
