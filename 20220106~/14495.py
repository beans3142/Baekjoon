arr=[0,1,1,1]
n=int(input())
for i in range(4,n+1):
    arr.append(arr[-1]+arr[-3])

print(arr[n])
