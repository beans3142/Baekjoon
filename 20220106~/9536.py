from sys import stdin
input=stdin.readline

t=int(input())
for i in range(t):
    case=[*input().split()]
    foxsays=[1]*len(case)
    while True:
        try:
            sound=input().rstrip().split(' goes ')[1]
            for i in range(len(case)):
                if sound==case[i]:
                    foxsays[i]=0
        except:
            break
    for i in range(len(case)):
        if foxsays[i]:
            print(case[i],end=' ')
    print()
