ps=input()
stack=['']
score=0
addscore=0
mul=1

for i in ps:
    if stack[-1]=='(' and i==')':
        mul//=2
        if ableAdd:
            addscore=2
            ableAdd=False
        else:
            addscore=0
        score+=addscore*mul
        stack.pop()
    elif stack[-1]=='[' and i==']':
        mul//=3
        if ableAdd:
            addscore=3
            ableAdd=False
        else:
            addscore=0
        score+=addscore*mul
        stack.pop()
    else:
        if i=='(':
            ableAdd=True
            mul*=2
        if i=='[':
            ableAdd=True
            mul*=3
        addscore=0
        stack.append(i)
        
if len(stack)==1:
    print(score)
else:
    print(0)
