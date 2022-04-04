from sys import stdin
input=stdin.readline

n,b=map(int,input().split())
arr=[list(map(int,input().split())) for i in range(n)]

def mul(arr1,arr2):
    arr3=[[0 for i in range(n)]for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                arr3[i][j]+=(arr1[i][k]*arr2[k][j])

    for i in range(n):
        for j in range(n):
            arr3[i][j]=arr3[i][j]%1000
    
    return arr3

a=[[0 if i!=j else 1 for i in range(n)] for j in range(n)]
r=arr
while b:
    if b%2==1:
        a=mul(a,r)
    r=mul(r,r)
    b>>=1

for i in a:
    print(*i)
