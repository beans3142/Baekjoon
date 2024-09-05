s=input()
bef=''
c1=0
c2=0
for i in s:
    if bef!=i:
        bef=i
        if i=='0':
            c1+=1
        else:
            c2+=1
print(c2+c1-max(c2,c1))
