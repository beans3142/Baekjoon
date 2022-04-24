n=int(input())
t=[1,1,2,5]

def gett(x):
    val=0
    for i in range(x):
        val+=(t[~i]*t[i])
    return val

for i in range(4,n+1):
    t.append(gett(i))

print(t[n])
