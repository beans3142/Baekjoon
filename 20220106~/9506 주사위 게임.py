#9506 약수의 합
nl=[];ns=0

while True:
    n=int(input())
    nl=[];ns=0
    if n==-1:
        break
    elif n%2==0:
        for i in range(1,n//2+1):
            if n%i==0:
                nl.append(i)
                ns+=i
        if ns==n:
            print(n,'=',end=' ')
            for j in nl:
                if j == n//2:
                    print(j)
                    continue
                print(j,'+',end=' ')
        else:
            print(n,'is NOT perfect.')
    else:
        print(n,'is NOT perfect.')

#https://www.acmicpc.net/problem/9506
