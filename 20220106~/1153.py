isprime=[1]*1000001
prime=[]
for i in range(2,1000001):
    if isprime[i]==0:
        continue
    else:
        prime.append(i)
        for j in range(i+i,1000001,i):
            isprime[j]=0
