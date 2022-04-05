s=input()

def rv(w):
    if w.islower():
        return w.upper()
    else:
        return w.lower()

for i in s:
    print(rv(i),end='')
    
'''
공백 처리 제대로 했는가,

in
hel lo wOr ld

out
HEL LO WoR LD
'''
