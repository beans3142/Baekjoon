for i in range(int(input())):
    total=sum(range(65,65+26))
    s=input()
    for w in set(s):
        total-=ord(w)
    print(total)
