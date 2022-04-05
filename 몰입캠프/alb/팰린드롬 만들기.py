import math

w=input()

l=len(w)
if l==1:
    print(1)
elif l==2:
    if w[0] != w[1]:
        print(3)
    else:
        print(2)
else:
    for i in range(l):
        is_p=True
        if l%2:
            l1=w[:math.ceil(l/2)+(i-1)//2]
            l2=w[math.ceil(l/2)+(i)//2:]
        else:
            l1=w[:math.ceil(l/2)+(i+1)//2]
            l2=w[math.ceil(l/2)+(i)//2:]
        for i in range(len(l2)):
            if l1[-len(l2)+i] != l2[-1-i]:
                is_p=False
                break
        if is_p:
            print(len(l1)-len(l2))
            break
    if not is_p:
        print(l-1)
