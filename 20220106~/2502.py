from sys import stdin
input=stdin.readline
arr=[[0,0],[1,0],[0,1]]

d,k=map(int,input().split())

for i in range(30):
    arr.append([arr[-1][0]+arr[-2][0],arr[-1][1]+arr[-2][1]])

x=arr[d][0]
y=arr[d][1]

for i in range(1,100000):
    if (k-i*x)%y==0:
        print(i)
        print((k-i*x)//y)
        break
