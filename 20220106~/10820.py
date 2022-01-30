try:
    while True:
        s=input()
        arr=[0]*4
        for w in s:
            arr[0]+=w.islower()
            arr[1]+=w.isupper()
            arr[2]+=w.isdigit()
            arr[3]+=w==' '
        print(*arr)
except:
    pass
