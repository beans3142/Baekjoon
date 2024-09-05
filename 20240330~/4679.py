while True:
    h,u,d,f=map(lambda x:int(x)*100,input().split())
    if h==0:
        break
    now=day=0
    f//=100
    cu=u
    while 1:
        day+=1
        now+=cu
        if now>h:
            break
        now-=d
        if now<0:
            break
        cu=cu-u*(f)//100
        if cu<=0: cu=0
    if now>h:
        print(f'success on day {day}')
    else:
        print(f'failure on day {day}')
