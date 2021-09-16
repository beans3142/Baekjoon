w=input()

for i in range(len(w)//2,len(w)):
    l1=w[:i]
    l2=w[i+1:]
    if l1 and l2:
        if_pal=True
        for j in range(min(len(l1),len(l2))):
            if l1[-1-j] != l2[j]:
                is_pal=False
                break
        if is_pal:
            for x in range(x,max(len(l1),len(l2))):
                print(x)
            
        
