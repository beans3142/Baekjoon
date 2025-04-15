n=int(input())
p=False
for i in range(2,11):
    s=[]
    m=n
    while m:
        s+=[m%i]
        m//=i
    l=0
    r=len(s)-1
    while s[l]==s[r] and l<r:
        l+=1
        r-=1
    if r<=l:
        p=True
        print(i,' ',*s,sep="")
if not p:print("NIE")
    
    
