#https://www.acmicpc.net/problem/21774

# n개의 입력을 #으로 분리해서 dict에 key , value 저장
# q개의 입력을 #으로 분리해서 start,end,value 이런식으로 3개에 나눠서 저장

# 로그가 발생한 순서대로 입력 => 굳이 정렬 시킬 필요 없이 이미 정렬된 형태


'''
from sys import stdin
input=stdin.readline

n,q=map(int,input().split())

arr={}
for i in range(n):
    arr[i]=input().rstrip().split('#')
    
for i in range(q):
    start,end,lv=input().rstrip().split('#')
    cnt=0
    for j in range(n):
        if start<=arr[j][0]<=end:
            cnt+=(arr[j][0]>=lv)
        elif arr[j][0]>end:
            break
    print(cnt)
'''


'''
from sys import stdin
input=stdin.readline

n,q=map(int,input().split())

def from_to(value,l):
    start=0
    end=l
    while start<=end:
        try:
            mid=(start+end)//2
            if arr[mid][0]<value<arr[mid+1][0]:
                return mid
            elif arr[mid][0]>value:
                end=mid-1
            else:
                start=mid+1
        except:
            return l
    return mid

arr={}

for i in range(n):
    arr[i]=input().rstrip().split('#')

for i in range(q):
    start,end,lv=input().rstrip().split('#')
    cnt=0
    for i in range(from_to(start),from_to(end)):
        cnt+=(arr[i][1]>=lv)
    print(cnt)
'''
# 맞음 
'''
from sys import stdin
input=stdin.readline

n,q=map(int,input().split())

arr={i+1:[] for i in range(6)}

def b(value,level,l):
    s=0
    e=l
    while s<e:
        mid=(s+e)//2
        if arr[level][mid]==value:
            e=mid
        elif value < arr[level][mid]:
            e=mid
        elif arr[level][mid]<value:
            s=mid+1
    return e

for i in range(n):
    date,lv=input().rstrip().split('#')
    arr[int(lv)].append(date)

for i in range(q):
    start,end,lv=input().rstrip().split('#')
    cnt=0
    for i in range(int(lv),7):
        #print(b(end+'',i,len(arr[i])),b(start,i,len(arr[i])))
        cnt+=b(end+'',i,len(arr[i]))-b(start,i,len(arr[i]))
    print(cnt)
'''
'''
from sys import stdin
import bisect

input=stdin.readline

n,q=map(int,input().split())

arr={i+1:[] for i in range(6)}

for i in range(n):
    date,lv=input().rstrip().split('#')
    arr[int(lv)].append(date)

for i in range(q):
    start,end,lv=input().rstrip().split('#')
    cnt=0
    for i in range(int(lv),7):
        if arr[i]:
            s_idx=bisect.bisect_left(arr[i],start)
            e_idx=bisect.bisect_right(arr[i],end)
            cnt+=e_idx-s_idx
    print(cnt)
'''
#
'''
from sys import stdin

input=stdin.readline

n,q=map(int,input().split())

arr={i+1:[] for i in range(6)}

for i in range(n):
    date,lv=input().rstrip().split('#')
    arr[int(lv)].append(date)

for i in range(q):
    start,end,lv=input().rstrip().split('#')
    cnt=0
    for i in range(int(lv),7):
        if arr[i] and not(arr[i][0]>end or arr[i][-1]<start) :
            for j in range(len(arr[i])):
                if start<=arr[i][j]<=end:
                    cnt+=1
    print(cnt)
'''
