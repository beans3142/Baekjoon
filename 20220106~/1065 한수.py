#백준 1065번 한수 https://www.acmicpc.net/problem/1065

n=input()
total=0

if int(n)<100:
    total+=int(n)

else:
    for i in range(100,int(n)+1):
        i=str(i)
        if int(i[0])-int(i[1])==int(i[1])-int(i[2]):
            total+=1
    total+=99

print(total)
    
