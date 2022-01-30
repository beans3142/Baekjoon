n = int(input())
sum = 0
while 1:
    five = n//5
    if five == 0:
        break
    sum += five
    n -= five*5
while 1:
    three = n//3
    if three == 0:
        break
    sum += three
    n -= three*3
if n != 0:
    print(-1)
else:
    print(sum)
