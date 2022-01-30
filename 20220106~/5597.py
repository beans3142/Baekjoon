from sys import stdin
input=stdin.readline
choolsuk=[1]+[0]*30
for i in range(28):
    choolsuk[int(input())]=1

for i in range(31):
    if choolsuk[i]==0:
        print(i)
