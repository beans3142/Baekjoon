from sys import stdin
input=stdin.readline
cnt=0
while True:
    o,w=map(int,input().split())
    if o==w==0:
        break
    alive=True
    while True:
        act,amount=input().rstrip().split()
        if act=='#' and amount=='0':
            break
        if alive:
            amount=int(amount)
            if act=='F':
                w+=amount
            elif act=='E':
                w-=amount
            if w<=0:
                alive=False
    if alive:
        if 0.5*o<w<2*o:
            print(f'{cnt+1} :-)')
        else:
            print(f'{cnt+1} :-(')
    else:
        print(f'{cnt+1} RIP')
    cnt+=1
        
