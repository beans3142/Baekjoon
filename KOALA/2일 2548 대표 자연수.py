from sys import stdin
input=stdin.readline
n=int(input())
arr=sorted(map(int,input().split()))

n_arr=[arr[0]]
mn=10**10
mn_num=arr[0]

for i in range(1,len(arr)):
    n_arr.append(n_arr[i-1]+arr[i])

mn=n_arr[-1]-n_arr[0]-arr[0]*(n-1)

if len(arr)==1:
    print(arr[0])
    exit()
else:
    for i in range(1,len(arr)):
        sum_count=((arr[i]*i)-n_arr[i-1])+((n_arr[-1]-n_arr[i])-arr[i]*(n-1-i))
        if sum_count<mn:
            mn=sum_count
            mn_num=arr[i]

print(mn_num)
