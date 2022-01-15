for i in range(3):
    s=input()
    mx=1
    idx=1
    stack=1
    while idx<8:
        if s[idx-1]==s[idx]:
            stack+=1
        else:
            stack=1
        mx=max(mx,stack)
        idx+=1
    print(mx)
