a=[]
r=''
for _ in range(int(input())):
    for i in input()+'_':
        if i.isdigit():
            r+=i
        else:
            if r:
                a.append(int(r))
                r=''
for i in sorted(a):
    print(i)
