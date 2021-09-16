from sys import stdin

input=stdin.readline

l,c=map(int,input().split())
spelling=input().rstrip().split()
spelling.sort()

def dfs(word,_idx,jaeum,moeum):
    if len(word)==l:
        if jaeum>1 and moeum>0:
            print(''.join(word))
        return
    for i in range(_idx+1,c):
        is_moeum = spelling[i] in ['a','e','i','o','u']
        dfs(word+[spelling[i]],i,jaeum+(not is_moeum),moeum+is_moeum)

for idx,i in enumerate(spelling):
    is_moeum= i in ['a','e','i','o','u']
    dfs([i],idx,not is_moeum,is_moeum)
