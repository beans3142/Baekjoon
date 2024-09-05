n,k=map(int,input().split())
nowsum=list(map(int,list(bin(n)[2:])))[::-1]
cnt1=nowsum.count(1)
ans=0
while cnt1>k:
    idx=nowsum.index(1)
    ans+=2**idx
    nowsum[idx]+=1
    rmv=-1
    while nowsum[idx]==2:
        nowsum[idx]=0
        idx+=1
        rmv+=1
        if idx<len(nowsum):
            nowsum[idx]+=1
        else:
            nowsum.append(1)
    cnt1-=rmv

print(ans)