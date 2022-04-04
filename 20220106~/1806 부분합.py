import sys
input=sys.stdin.readline
'''
n,s=map(int,input().split())

arr=list(map(int,input().split()))+[0]
'''
n,s=10,10

arr=[1,1,1,1,1,1,1,1,1,1]+[0]

front=0
back=1
len_arr=100001
total=arr[0]

while back<len(arr):
    while total <=s and back < len(arr):
        total+=arr[back]
        back+=1
    while total>s and front<=back:
        total-=arr[front]
        front+=1
    len_arr=min(back-front,len_arr)
    while total<=s and front<=back<len(arr):
        total-=arr[front]
        total+=arr[back]
        back+=1
        front+=1
        if back==len(arr):
            break
        
    
    
if len_arr != 100001:
    print(len_arr)
else:
    print(0)
