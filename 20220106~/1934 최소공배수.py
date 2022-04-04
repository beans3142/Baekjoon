t=int(input())

for i in range(t):
    a,b=map(int,input().split())
    n1,n2=a,b
    j=2
    if max(a,b)%min(a,b)==0:
        print(max(a,b))
        continue
    while max(a,b) >= j:
        if a%j==0 and b%j==0:
            a//=j ; b//=j
            j=2
            continue
        j+=1
    print(max(n1,n2)*min(a,b))
