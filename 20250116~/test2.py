for n in range(1,5):
    for k in range(1,50):
        
        def bitrev(x,N):
            y=0
            for _ in range(N):
                y=(y<<1)|(x&1)
                x>>=1
            return y

        #n,k=map(int,input().split())
        le=1<<n
        q=k//le
        r=k%le
        ans1=[q]*le
        for i in range(le):
            if bitrev(i,n)<r:
                ans1[i]+=1
        #n,k=map(int,input().split())
        le=2**n
        #print(1 if k%le else 0)
        left=k%le
        ans=[k//le for i in range(le)]
        add=[0]*le
        for i in range(n):
            for j in range(0,le,le//2**(i+1)):
                if left and add[j]==0:
                    ans[j]+=1
                    left-=1
                    add[j]=1
        if ans!=ans1:
            print(n,k,ans,ans1)
