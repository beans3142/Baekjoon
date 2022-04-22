from sys import stdin
input=stdin.readline

n=int(input())

fibo=[0,1]

for i in range(77):
    fibo.append(fibo[-1]+fibo[-2])

while True:
    for i in range(77):
        if fibo[i]>n:
            break

    if n==fibo[i-1]:
        print(n)
        exit()
    n-=fibo[i-1]

