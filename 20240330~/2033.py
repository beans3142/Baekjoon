arr=list(map(int,list(input())))[::-1]
for i in range(len(arr)):
    if arr[i]>4:
        arr[i]=0
        if i+1!=len(arr):
            arr[i+1]+=1
        else:
            arr.append(1)
    
print(*arr[::-1],sep="")
