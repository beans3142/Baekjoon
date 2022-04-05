arr=[]
for i in range(10):
    arr.append(int(input()))

mean=sum(arr)//10
arr.sort()
common=arr[0]
maxstack=1
stack=1
for i in range(1,10):
    if arr[i]==arr[i-1]:
        stack+=1
        if stack>maxstack:
            maxstack=stack
            common=arr[i]
    else:
        stack=1

print(mean)
print(common)
