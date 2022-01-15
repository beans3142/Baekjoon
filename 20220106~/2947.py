arr=list(map(int,input().split()))
changed=True
while changed:
    changed=False
    for i in range(4):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            print(*arr)
            changed=True

