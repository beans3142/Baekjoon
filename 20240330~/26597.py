from sys import stdin

mn=-10**18-1
mx=10**18+1
flag_able=False
ans=0
for _ in range(int(input())):
    x,t=input().rstrip().split()
    if t=='^':
        mn=max(int(x),mn)
    else:
        mx=min(int(x),mx)
    if mn<mx-1<=mn+1<mx and not flag_able:
        flag_able=True
        ans=_+1
    if mn+1>=mx:
        print("Paradox!")
        print(_+1)
        exit()
if flag_able: print("I got it!\n",ans,sep="")
else:print("Hmm...")
