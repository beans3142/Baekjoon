from collections import defaultdict

s=input()
dd=defaultdict(int)
for i in s:
    dd[i]+=1

odd=''
front=''

for i in sorted(dd):
    if dd[i]%2:
        if odd:
            print("I'm Sorry Hansoo")
            exit()
        else:
            odd=i
    front+=i*(dd[i]//2)

print(front+odd+front[::-1])
