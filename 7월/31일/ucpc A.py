arr=input()

printed=False
a=''
b=''
try:
    for i in range(3):
        a+=arr[i]
        for j in range(3):
            narr=''
            b=arr[~j]+b
            for n in range(int(a),int(b)+1):
                narr+=str(n)
            if narr==arr:
                if printed==False:
                    print(int(a),int(b))
                    printed=True
                exit()
        b=''
except:
    if printed==False:
        print(int(arr),int(arr))
        printed=True
    exit()
