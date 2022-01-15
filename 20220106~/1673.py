from sys import stdin
input=stdin.readline

while True:
    try:
        n,k=map(int,input().split())
        total=n
        while n//k:
            total+=n//k
            n=n//k+n%k
        print(total)
    except:
        break
