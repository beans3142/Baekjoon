import sys
input=sys.stdin.readline
n,s=map(int,input().split())

arr=list(map(int,input().split()))+[0]

front=-1
back=0
total=arr[0]
len_arr=100001

while front<len(arr)-2 or back<len(arr)-1:
    try:
        if total>=s:
            front+=1
            total-=arr[front]
        if total<s:
            back+=1
            total+=arr[back]
        if total>=s:
            len_arr=min(len_arr,back-front)
    except IndexError:
        break

if len_arr < 100001:
    print(len_arr)
else:
    print(0)
