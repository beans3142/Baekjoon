import sys ; input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
swap=0
def merge(l):
    global swap
    if len(l)==1:
        return
    mid=len(l)//2
    l1=l[:mid]
    l2=l[mid:]
    merge(l1)
    merge(l2)
    i1=0
    i2=0
    idx=0
    ds=0
    while i1<len(l1) and i2<len(l2):
        if l1[i1]<=l2[i2]:
            l[idx]=l1[i1]
            idx+=1
            i1+=1
            swap+=ds
        else:
            ds+=1
            l[idx]=l2[i2]
            idx+=1
            i2+=1
    while i1<len(l1):
        l[idx]=l1[i1]
        idx+=1
        i1+=1
        swap+=ds
    while i2<len(l2):
        l[idx]=l2[i2]
        idx+=1
        i2+=1
merge(arr)
print(swap)
