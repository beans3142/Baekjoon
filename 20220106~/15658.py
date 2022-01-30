from sys import stdin
input=stdin.readline

def bt(value,idx,pl,mi,mu,di):
    global mx,mn
    if idx==n:
        mx=max(mx,value)
        mn=min(mn,value)
        return
    if pl>0:
        bt(value+arr[idx],idx+1,pl-1,mi,mu,di)
    if mi>0:
        bt(value-arr[idx],idx+1,pl,mi-1,mu,di)
    if mu>0:
        bt(value*arr[idx],idx+1,pl,mi,mu-1,di)
    if di>0:
        bt(abs(value)//arr[idx]*(-1 if value<0 else 1),idx+1,pl,mi,mu,di-1)
        
n=int(input())
arr=list(map(int,input().split()))
mx=-(10**11)
mn=10**11
bt(arr[0],1,*map(int,input().split()))
print(mx)
print(mn)
