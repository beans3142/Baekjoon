n=int(input())

for i in range(int(n**0.5)+1):
    for j in range(int(n**0.5)+1):
        for k in range(int(n**0.5)+1):
            if i*i+j*j+k*k==n:
                print(bool(i)+bool(j)+bool(k))
                exit()
print(4)
