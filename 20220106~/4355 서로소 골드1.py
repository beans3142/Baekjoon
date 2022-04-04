'''
def yaksu(n):
    global s
    if 1<n<4:
        try:
            s[n]+=1
            return
        except KeyError:
            s[n]=1
            return
    for i in range(2,int(n**0.5)+1):
        try:
            if n%i==0:
                s[i]=1
                #s[i]+=1
                return yaksu(n//i)
        except KeyError:
            #s[i]=1
            return yaksu(n//i)


while True:
    n=int(input())
    if n==0:
        break
    s={}
    yaksu(n)
    gaesu=1
    for i in s:
        gaesu*=s[i]+1
    print(n-gaesu)
'''
def yaksu(n):
    global s
    if 1<n<4:
        if s[-1] != n:
            s.append(n)
        return
    for i in range(2,n+1):
        if n%i==0:
            if s[-1] != i:
                s.append(i)
            return yaksu(n//i)


while True:
    n=int(input())
    if n==0:
        break
    s=[1]
    yaksu(n)
    gaesu=0
    for i in range(1,len(s)):
        gaesu+=(n-1)//s[i]#+n%s[i]
        for j in range(1,len(s)):
            if i!=j:
                gaesu-=(n-1)//(s[i]*s[j])#+n%(s[i]*s[j])
    print(n-1-gaesu)
                
            
