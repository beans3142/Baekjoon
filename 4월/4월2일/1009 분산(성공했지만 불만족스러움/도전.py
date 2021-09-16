T=int(input())

for i in range(T):
    a,b=map(int,input().split())
    a=a%10
    if a==0:
        print(10)
    elif a==1:
        print(1)
    elif a==2:
        #2 4 8 6
        n=b%4
        if n == 0:
            n=4
        print(2**n%10)
    elif a==3:
        #3 9 7 1
        n=b%4
        if n == 0:
            n=4
        print(3**n%10)
    elif a==4:
        #4 6 2 8
        n=b%4
        if n == 0:
            n=4
        print(4**n%10)
    elif a==5:
        print(5)
    elif a==6:
        print(6)
    elif a==7:
        #7 9 3 1
        n=b%4
        if n == 0:
            n=4
        print(7**n%10)
    elif a==8:
        #8 4 2 6
        n=b%4
        if n == 0:
            n=4
        print(8**n%10)
    elif a==9:
        #9 1
        n=b%2
        if n == 0:
            n=2
        print(9**n%10)
