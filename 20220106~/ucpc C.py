a,d,k=map(int,input().split())

win=d
total=[]
minute=a
while True:
    rate=win/100*a
    total.append(rate*minute if rate<1 else 1*minute)
    if win>=100:
        break
    win*=(1+k/100)

print(sum(total)/len(total))
