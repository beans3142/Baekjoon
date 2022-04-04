from sys import stdin
input=stdin.readline
n=int(input())
arr=[[0 for i in range(n)]for j in range(n)]
arr2=[[0 for i in range(n)]for j in range(n)]
for i in range(n):
    line=list(map(int,input().split()))
    for j in range(n):
        arr[i][j]=line[j]
        arr2[i][j]=line[j]

zero_cnt=0
one_cnt=0
while True:
    over=False
    for i in range(n):
        xcnt=0
        ycnt=0
        for j in range(n):
            if arr[i][j]==1:
                xcnt+=1
            if arr[j][i]==1:
                ycnt+=1
        if xcnt>n//2:
            zero_cnt+=1
            for j in range(n):
                arr[i][j]=abs(arr[i][j]-1)
            over=True
            continue
        if ycnt>n//2:
            zero_cnt+=1
            for j in range(n):
                arr[j][i]=abs(arr[j][i]-1)
            over=True
            continue
    if not over:
        for i in range(n):
            for j in range(n):
                zero_cnt+=arr[i][j]
        break

while True:
    over=False
    for i in range(n):
        xcnt=0
        ycnt=0
        for j in range(n):
            if arr2[i][j]==0:
                xcnt+=1
            if arr2[j][i]==0:
                ycnt+=1
        if xcnt>n//2:
            one_cnt+=1
            for j in range(n):
                arr2[i][j]=abs(arr2[i][j]-1)
            over=True
            continue
        if ycnt>n//2:
            one_cnt+=1
            for j in range(n):
                arr2[j][i]=abs(arr2[j][i]-1)
            over=True
            continue
    if not over:
        for i in range(n):
            for j in range(n):
                one_cnt+=abs(arr2[j][i]-1)
        break
print(min(one_cnt,zero_cnt))

