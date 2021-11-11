from sys import stdin
input=stdin.readline

a=sorted(map(int,input().split()))
if a[1]-a[0]<a[2]-a[1]:
    print(2*a[1]-a[0])
elif a[1]-a[0]>a[2]-a[1]:
    print(a[0]+a[2]-a[1])
else:
    print(a[2]+a[1]-a[0])

