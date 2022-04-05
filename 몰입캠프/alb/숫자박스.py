from sys import stdin
input=stdin.readline

# 여기 부분 중점적으로 보면 될 듯
def bs(x):
    l=0
    r=n-1
    while l<=r:
        mid=(l+r)//2
        if box[mid]<x:
            l=mid+1
        elif box[mid]==x:
            return 1
        else:
            r=mid-1
    return 0

n=int(input())
box=sorted(map(int,input().split()))
m=int(input())
q=list(map(int,input().split()))

for i in q:
    print(bs(i))
