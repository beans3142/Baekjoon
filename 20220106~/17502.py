n=int(input())
l=0
r=n-1
s=[*input()]
while l<=r:
    if s[l]=='?':
        if s[r]=='?':
            s[l]='a'
            s[r]='a'
        else:
            s[l]=s[r]
    elif s[r]=='?':
        s[r]=s[l]
    l+=1
    r-=1

print(''.join(s))
    
