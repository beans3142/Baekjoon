from sys import stdin
input=stdin.readline

def cmp(x,y):
    if int(x+y)>int(y+x):
        return False
    return True

k,n=map(int,input().split())
arr=[]
mx=0

for i in range(k):
    num=input().rstrip()
    mx=max(int(num),mx)
    arr.append(num)

mx=str(mx)
for i in range(n-k):
    arr.append(mx)

for i in range(n):
    for j in range(n-1-i):
        if cmp(arr[j],arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]

print(''.join(arr))
