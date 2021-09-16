from sys import stdin
input=stdin.readline

n=int(input())

arr=[(int(input()),i) for i in range(n)]
s_arr=sorted(arr)
mx=0

for i in range(n):
    mx=max(s_arr[i][1]-arr[i][1],mx)

print(mx+1)
