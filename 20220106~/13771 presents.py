from sys import stdin
input=stdin.readline

k={}
val=[]

for i in range(int(input())):
    a=input().rstrip()
    k[float(a)]=a
    val.append(float(a))

print(k[sorted(val)[1]])
