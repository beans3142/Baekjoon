def check(num,idx):
    if idx==n:
        case.append(num)
        return
    check(num+garr[idx],idx+1)
    check(num,idx+1)

n=4
garr=[5,6,7,8]
case=[]
check(0,0)
print(n)
print(*case)
