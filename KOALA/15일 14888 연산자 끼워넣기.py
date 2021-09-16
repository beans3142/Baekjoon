#https://www.acmicpc.net/problem/14888

# 백트래킹으로 모든 경우 탐색? <- 이게 맞는지는 아직 잘 모르겠음.
# + - * / *나 /라고 먼저 계산하고 그런 것은 없음.

from sys import stdin
input=stdin.readline

n=int(input())

sootja=list(map(int,input().split()))

pl,mi,mu,di=list(map(int,input().split()))

mn=1000000000
mx=-1000000000

def compute(arr,plus,minus,mult,divi):
    global mn,mx
    if len(arr)==1:
        mn=min(arr[0],mn)
        mx=max(arr[0],mx)
        return
    if plus:
        compute([arr[0]+arr[1]]+arr[2:],plus-1,minus,mult,divi)
    if minus:
        compute([arr[0]-arr[1]]+arr[2:],plus,minus-1,mult,divi)
    if mult:
        compute([arr[0]*arr[1]]+arr[2:],plus,minus,mult-1,divi)
    if divi:
        if arr[0]<0:
            arr[0]=-arr[0]
            compute([-(arr[0]//arr[1])]+arr[2:],plus,minus,mult,divi-1)
        else:
            compute([arr[0]//arr[1]]+arr[2:],plus,minus,mult,divi-1)

compute(sootja,pl,mi,mu,di)

print(mx)
print(mn)
