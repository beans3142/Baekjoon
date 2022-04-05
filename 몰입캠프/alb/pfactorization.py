n=int(input())
while n:
    div=False
    for i in range(2,n):
        if n%i==0:
            print(i)
            n//=i
            div=True
            break
    if not div:
        print(n)
        break
