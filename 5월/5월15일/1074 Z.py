#https://www.acmicpc.net/problem/1074

# 총 블럭의 개수 = 4^n
# n당 행의 개수 = 2^n

n,r,c=map(int,input().split())

#matrix=[[i for i in range(2**n)]for _ in range(2**n)]
num=0

while n>1:
    ran=2**(n-1) # 빗변의 길이 1, 2, 4, 8 ...
    if r>= ran: # 만약 빗변의 길이의 절반보다 r이 크면
        if c>= ran: # 만약 빗변의 길이의 절반보다 c도 크면
            num+=3*4**(n-1) #1~4분면이라 햇을때 4분면에 위치 1~3분면 모두 이동함
            r-=ran
            c-=ran
        else:
            num+=2*4**(n-1)
            r-=ran
    else:
        if c>=ran:
            num+=4**(n-1)
            c-=ran

    n-=1

if r==0:
    if c==0:
        print(num)
    else:
        print(num + 1)
else:
    if c == 0:
        print(num + 2)
    else:
        print(num + 3)
            
            
