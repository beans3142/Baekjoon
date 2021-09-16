from sys import stdin
input=stdin.readline

l,c=map(int,input().split())
spelling=sorted(input().rstrip().split())
moeum_list=['a','e','i','o','u']

def dfs(word,_idx,jaeum,moeum):
    if len(word)==l:
        if jaeum>1 and moeum>0:
            print(''.join(word))
        return
    for i in range(_idx+1,c):
        is_moeum = spelling[i] in moeum_list
        dfs(word+[spelling[i]],i,jaeum+(not is_moeum),moeum+is_moeum)

dfs([],-1,0,0)
