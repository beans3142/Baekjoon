from sys import stdin
input=stdin.readline

n,s=map(int,input().split())
arr=[*map(int,input().split())]
l=0
r=0
total=0
ans=100001

while l<n:
    if total<s and r<n:
        total+=arr[r]
        r+=1
    elif total>=s or r==n:
        if total>=s:
            ans=min(ans,r-l)
        total-=arr[l]
        l+=1
    
    
print(ans if ans!=100001 else 0)
