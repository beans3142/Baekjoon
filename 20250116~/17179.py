from sys import stdin
input=stdin.readline

# 시간복잡도 : 유효성 검사 O(M) 검사 횟수 O(logL) 를 N번 반복하므로
# 최종 시간복잡도는 O(NMlogL)
# 대략 2000만 정도.

def check(d): # 검사 함수
    # 길이가 d 이상이 되면 자른다.
    piece=0
    now=0
    for i in range(m+1):
        now+=arr[i]
        if now>=d:
            piece+=1
            now=0
    return piece>=q
        

n,m,l=map(int,input().split())
arr=[int(input()) for i in range(m)]+[l]
for i in range(m,0,-1):
    arr[i]=arr[i]-arr[i-1]

for i in range(n):
    q=int(input())+1
    mn=0
    mx=l
    ans=0
    while mn<=mx:
        mid=(mn+mx)//2
        res=check(mid) 
        if res:
            ans=max(mid,ans)
            mn=mid+1
        else:
            mx=mid-1
    print(ans)
