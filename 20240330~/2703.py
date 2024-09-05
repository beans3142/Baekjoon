for _ in range(int(input())):
    s=input()
    c=input()
    print(*[c[ord(i)-65] if i.isalpha() else i for i in s],sep='')
