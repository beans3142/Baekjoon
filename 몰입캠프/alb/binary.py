def bi(n):
    biN=''
    if n<2:
        return str(n)
    biN=bi(n//2)+str(n%2)
    return biN
    
print(bi(int(input())))
