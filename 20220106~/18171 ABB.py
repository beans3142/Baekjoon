def manach(s,n):
    a=[0]*n
    r=p=0
    for i in range(n):
        if i<=r:
            a[i]=min(a[2*p-i],r-i)
        else:
            a[i]=0
        while (i-a[i]-1>=0 and i+a[i]+1<n and s[i-a[i]-1]==s[i+a[i]+1]):
            a[i]+=1
        if r<i+a[i]:
            r=i+a[i];
            p=i
    return a

n=int(input())
w='_'+'_'.join(input())+'_'

ans=manach(w,len(w))

cnt=0
mx=0
ans_w=0

print(n-max(ans))
