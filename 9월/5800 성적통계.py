from sys import stdin
input=stdin.readline
for i in range(int(input())):
    arr=sorted(map(int,input().split()[1:]))
    big_dif=0
    for j in range(1,len(arr)):
        big_dif=max(big_dif,arr[j]-arr[j-1])
    print(f'Class {i+1}\nMax {arr[-1]}, Min {arr[0]}, Largest gap {big_dif}')
    
