from sys import stdin
input=stdin.readline

for _ in range(int(input())):
    n,*arr=map(int,input().split())
    narr=[]
    able=True
    if n==0: continue
    elif n==1: narr=[arr[0]+i+1 for i in range(5)]
    else: 
        d=arr[1]-arr[0]
        for i in range(1,n):
            if arr[i]-d!=arr[i-1]:
                able=False
                break
        if able:
            for i in range(5):
                narr.append(arr[-1]+(i+1)*d)
    if narr:
        print(f'The next 5 numbers after {arr} are: {narr}')
    else:
        print(f'The sequence {arr} is not an arithmetic sequence.')