n=int(input())

for i in range(n):
    score=0
    scores=0
    ans=input()
    for i in range(len(ans)):
        if ans[i]=='O':
            score+=1
            scores+=score
        else:
            score=0
    print(scores)

# https://www.acmicpc.net/problem/8958

