plate=input()
h=10
for i in range(1,len(plate)):
    if plate[i-1] != plate[i]:
        h+=10
    else:
        h+=5

print(h)

#https://www.acmicpc.net/problem/7567
