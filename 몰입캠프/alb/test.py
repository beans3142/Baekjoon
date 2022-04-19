x=10000000

sieve=[]

def prime_list(n):
  global sieve
  sieve=[True]*n
  
  m=int(n**0.5)
  for i in range(2,m+1):
    if sieve[i]==True:
      for j in range(i+i,n,i):
        sieve[j]=False
        
prime_list(x) 
  
prime=[1]*(x)
prime[0]=prime[1]=0
for i in range(2,x):
  if prime[i]==0:
    continue
  for j in range(i+i,x,i):
    prime[j]=0
