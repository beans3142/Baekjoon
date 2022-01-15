for i in range(int(input())):
    a, b = input().split()
    arr = []
    for j in range(len(a)):
        if ord(a[j]) > ord(b[j]):
            arr.append(26 - (ord(a[j])-ord(b[j])))
        else:
            arr.append(ord(b[j]) - ord(a[j]))
    print("Distances:", *arr)
