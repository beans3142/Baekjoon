from sys import stdin
input=stdin.readline

i=1
while True:
    try:
        s1,s2=input().rstrip().split('=')
        x=10**50
        r1=eval(s1)
        r2=eval(s2)
        nx=r1//x-r2//x
        y=(r2%x-r1%x)
        print("Equation #",i,sep='')
        i+=1
        if nx==0 and y!=0:
            print('No solution.')
        elif nx==0 and y==0:
            print('Infinitely many solutions.')
        else:
            print('x = %.6f'%(y/nx))
        print()
    except:
        break
        
        
        
