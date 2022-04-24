from sys import stdin
input=stdin.readline

n=int(input())

arr=[0,1,0,1,1,1]
for i in range(6,n+1):
    if arr[-1]==0 or arr[-3]==0 or arr[-4]==0:
        arr.append(1)
    else:
        arr.append(0)

print("SK" if arr[n] else "CY")
