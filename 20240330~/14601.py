def recur(n):
    if n==1:
        return ['XX','XO']
    leftup=recur(n-1)
    top=leftup[0]+leftup[0][::-1]+leftup[1]+leftup[1][::-1]
    bottom=leftup[1]+leftup[0]+leftup[0]+leftup[1]
    nowline=[top,\
             bottom]
    return nowline
    

n=int(input())
res=recur(n)
res=res[0]+res[1]
for i in range(4**n):
    print(res[i],end='')
    if (i+1)%(2**n)==0:
        print()
    
