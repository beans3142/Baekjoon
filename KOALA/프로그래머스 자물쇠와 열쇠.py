from sys import stdin
from 비교용 import *
from random import*

key=[[0,0,1],[0,1,1],[0,0,1]]
lock=[[1, 1, 1,1], [1, 1, 1,1], [0, 1, 1,1],[0,1,1,1]]


def make_big_table(arr1,arr2):
    l1=len(arr1)-1
    l2=len(arr2)
    n_arr=[[0 for i in range(l1+l2)] for i in range(l1)]
    for i in range(l2):
        n_arr.append([0 for i in range(l1)]+arr2[i])

    return n_arr,len(n_arr)

def rotate(arr1):
    l1=len(arr1)
    rotated=[arr1,[],[],[]]
    for _ in range(3):
        at_rotated=[[0 for i in range(l1)]for i in range(l1)]
        for i in range(l1):
            for j in range(l1):
                at_rotated[~j][i]=rotated[_][i][j]
        rotated[_+1]=at_rotated
    return rotated

def sol(key,lock):
    l1=len(key)
    l2=len(lock)
    bigmap,mx_len=make_big_table(key,lock)
    rotated_keys=rotate(key)
    lock_hole=0
    for i in range(l2):
        for j in range(l2):
            if lock[i][j]==0:
                lock_hole+=1
    for rotated_key in rotated_keys:
        for i in range(mx_len):
            for j in range(mx_len):
                correct=0
                unable=False
                for ii in range(l1):
                    nowy=i+ii
                    for jj in range(l1):
                        nowx=j+jj
                        if l1-2<nowx<mx_len and l1-2<nowy<mx_len:
                            if rotated_key[ii][jj]==1 and bigmap[nowy][nowx]==0:
                                correct+=1
                            elif rotated_key[ii][jj]==bigmap[nowy][nowx]:
                                unable=True
                                break
                    if unable:
                        break
                if unable:
                    continue
                if correct==lock_hole:
                    return True
    return False

'''
tmpt=0
while True:
    tmpt+=1
    xxxx=randint(3,6)
    yyyy=randint(xxxx,10)
    key=([randint(0,10)<4 for i in range(xxxx)]for i in range(xxxx))
    lock=([randint(0,10)>3 for i in range(yyyy)]for i in range(yyyy))
    print(tmpt,'번째 시도 : ',end=' ')
    t1=solution(key,lock)
    t2=sol(key,lock)
    print(t1,t2)
    if t1!=t2:
        print('드디어 틀렸다!')
        for i in key:
            print(i)
        for j in lock:
            print(j)
        break'''

keys=[]
locks=[]
keys.append([[1,1,1],[1,1,1],[1,1,1]])
locks.append([[1,1,1],[1,1,1],[1,1,1]])
for i in range(len(keys)):
    print(sol(keys[i],locks[i]))
    print(solution(keys[i],locks[i]))
