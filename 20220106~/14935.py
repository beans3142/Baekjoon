from sys import stdin
input=stdin.readline

x=int(input())
bef=-1
while x!=bef:
    bef=x
    x=int(str(x)[0])*len(str(x))
print("FA")
