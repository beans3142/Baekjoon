fibo_list=[[1,0],[0,1],[1,2],[2,3]]
a=b=0
def fibo(n):
    global a,b
    if n < 5:
        a+=fibo_list[n-1][0]
        b+=fibo_list[n-1][1]
        print(a,b)
    else:
        if [fibo(n-1),fibo(n-2)] not in fibo_list:
            return fibo(n-1) + fibo(n-2)
        else:
            a+=fibo_list[n-1][0]+fibo_list[n-2][0]
            b+=fibo_list[n-1][1]+fibo_list[n-2][1]
            return 0

            
fibo(7)
print(fibo_list)

for i in range(int(input())):
    a=b=0
