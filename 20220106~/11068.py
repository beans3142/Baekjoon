from sys import stdin
input=stdin.readline

def is_true(arr):
    able=True
    for i in range(len(arr)//2):
        if arr[i]!=arr[~i]:
            able=False
    return able

def convert(n,b):
    ans=[]
    while n:
        ans.append(n%b)
        n//=b
    return ans
        
for t in range(int(input())):
    n=int(input())
    able=False
    for b in range(2,65):
        converted_n=convert(n,b)
        if is_true(converted_n):
            able=True
    if able:
        print(1)
    else:
        print(0)
