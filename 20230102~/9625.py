k=int(input())
fibo=[0,1]
for i in range(45):
    fibo.append(fibo[-1]+fibo[-2])
print(fibo[k-1],fibo[k])
