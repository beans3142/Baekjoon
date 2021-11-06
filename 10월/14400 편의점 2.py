from sys import stdin
input=stdin.readline

n=int(input())
arr1=[]
arr2=[]
for i in range(n):
    x,y=map(int,input().split())
    arr1.append(x)
    arr2.append(y)


arr1=sorted(arr1)
arr2=sorted(arr2)

mx=sorted(arr1)[n//2]
my=sorted(arr2)[n//2]

lensum=0
for i in range(n):
    lensum+=abs(mx-arr1[i])+abs(my-arr2[i])

print(lensum)
