f="12" if input()=="1" else "21"
l=[[0,0,0,0]for i in range(2)]
for i in range(9):
    a,b=map(int,input().split())
    l[i%2][a]^=(1<<b)
    e=l[i%2]
    if(e[1]&e[2]&e[3])|(14 in e)|(e[2]&4 and((e[1]&2 and e[3]&8)or(e[1]&8 and e[3]&2))):
        print(f[i%2])
        exit()
        
print(0)
