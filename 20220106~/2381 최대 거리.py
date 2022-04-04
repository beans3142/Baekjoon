from sys import stdin
input=stdin.readline
n=int(input())
ans=0
arr=[]
arr2=[]
arr3=[]
arr4=[]
for i in range(n):
    x,y=map(int,input().split())
    arr.append((x-y,x,y))
    arr2.append((x,y))
    arr3.append((x+y,x,y))
    arr4.append((y,x))

arr.sort()
arr2.sort()
arr3.sort()
arr4.sort()
ans=max(ans,(abs(arr[0][1]-arr[-1][1])+abs(arr[0][2]-arr[-1][2])),\
        (abs(arr2[0][0]-arr2[-1][0])+abs(arr2[0][1]-arr2[-1][1])),\
        (abs(arr3[0][1]-arr3[-1][1])+abs(arr3[0][2]-arr3[-1][2])),\
        (abs(arr4[0][0]-arr4[-1][0])+abs(arr4[0][1]-arr4[-1][1])))
print(ans)
