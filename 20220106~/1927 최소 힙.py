import sys
input=sys.stdin.readline

s=set()
same={}

for i in range(int(input())):
    order=int(input())
    if order:
        s.add(order)
        print(s,order   )
        try:
            same[order]+=1
        except KeyError:
            same[order]=1
        
    else:
        if s:
            for i in sorted(s):
                #print(i)
                print(s)
                if same[i]<2:
                    s.discard(i)
                same[i]-=1
                break
                '''
                try:
                    if same[i]>0:
                        same[i]-=1
                        break
                    s.discard(i)
                    break
                except KeyError:
                    s.discard(i)
                    break
                    '''
        else:
            print(0)
