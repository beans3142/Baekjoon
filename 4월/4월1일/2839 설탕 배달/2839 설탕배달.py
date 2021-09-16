N=int(input())

if N%5 == 0:
    print(N//5)
elif N==3:
    print(1)
elif N >5 and N != 7:
    if N%5 == 1:
        print(N//5+1)
    if N%5 == 2:
        print(N//5+2)
    if N%5 == 3:
        print(N//5+1)
    if N%5 == 4:
        print(N//5+2)
else:
    print(-1)
