import sys
input=sys.stdin.readline


n=int(input())
enroll={}

for i in range(n):
    age,name=input().rstrip().split()
    age=int(age)
    if age not in enroll:
        enroll[age]=[name]
    else:
        enroll[age].append(name)

for age in sorted(enroll):
    for name in enroll[age]:
        print(age,name)
