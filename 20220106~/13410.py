from sys import stdin
input=stdin.readline

n,k=map(int,input().split())
arr=[int(str(n*i)[::-1]) for i in range(1,k+1)]
    
print(max(arr))
