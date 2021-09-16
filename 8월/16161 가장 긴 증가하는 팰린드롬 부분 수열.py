def manach(s,n):
    a=[0]*n
    r=p=0
    for i in range(n):
        if i<=r:
            a[i]=min(a[2*p-i],r-i)
        else:
            a[i]=0
        while (i-a[i]-1>=0 and i+a[i]+1<n and s[i-a[i]-1]==s[i+a[i]+1] and (s[i-a[i]-1]==s[i+a[i]+1]==0 or(s[i-a[i]+1]>s[i-a[i]-1] and s[i+a[i]-1]>s[i+a[i]+1]))):
            a[i]+=1
        if r<i+a[i]:
            r=i+a[i];
            p=i
    return a
int(input())
w=[int(i) for i in '0'+'0'.join(input().split())+'0']

ans=manach(w,len(w))

mx=0
ans_w=0

#print(ans)
print(max(ans))
