import sys

input=sys.stdin.readline

n=int(input())
a=set(map(int,input().split()))

m=int(input())
b=list(map(int,input().split()))

for i in b:
    if i in a:
        print(1)
        continue
    print(0)

'''
for i in b:
    if a[0]<=i<=a[-1]:
        mn=0
        mx=len(a)-1
        while True:
            mid=(mn+mx)//2
            if a[mid]==i:
                print(1)
                break
            if mn>mx:
                print(0)
                break
            if a[mid]<i:
                mn=mid+1
            else:
                mx=mid-1
    else:
        print(0)
'''
