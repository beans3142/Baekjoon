import random

n,l=map(int,input().split())

s=0
sl=[]

if n==3 and l==2:
    print(1,2)
else:
    for i in range(l,101):
        if n!=1 and ((i-1)**2+(i-1))//2>n:
            break
        if i%2:
            s=n//i
            f=s-(i//2)
            b=s+(i//2)
            if (i*(f+b))//2==n:
                for x in range(-i//2+1,i//2+1):
                    if s+x>n:
                        break
                    sl.append(s+x)
                break
        else:
            s=n//i
            f=s-(i//2)+1
            b=s+(i//2)
            if (i*(f+b))//2==n:
                for x in range(-i//2+1,i//2+1):
                    if s+x>n:
                        break
                    sl.append(s+x)
                break
        
    if sl and (max(sl)<n or max(sl)==1):
        for i in sl:
            print(i,end=' ')
    else:
        print(-1)


'''
for i in range(10):
    n,l=random.randint(1,1000),random.randint(2,100)
    print(n,l)
    test(n,l)
    print()
'''
'''
s=0
sl=[]
is_true=False

if n%2:
    if l%4==0:
        l+=1
if n%2==0:
    if l%2==0:
        l+=1

for i in range(n//l+l//2+1,0,-1):
    if i < n:
        if (s==n and len(sl)>=l):
            is_true=True
            break
        if len(sl)>100:
            break
        else:
            if s<n:
                s+=i
                sl.append(i)
            elif s>n:
                s+=i
                sl.append(i)
                s-=sl.pop(0)

if is_true:
    for i in reversed(sl):
        print(i,end=' ')
else:
    print(-1)
'''
