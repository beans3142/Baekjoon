n=int(input())
line=[0]*n
arr_left=list(map(int,input().split()))
for idx,left in enumerate(arr_left):
    for j in range(n):
        if left==0 and line[j]==0:
            line[j]=idx+1
            break
        elif line[j]==0:
            left-=1
    print(line)
    
