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

w='_'+'_'.join(input())+'_'

ans=manach(w,len(w))

mx=0
ans_w=0

for i in ans:
    ans_w+=(i+1)//2

print(ans_w%10007)
