from sys import stdin
input=stdin.readline

case={chr(97+i):0 for i in range(26)}


s=stdin.read().replace('\n','').replace(' ','')

for i in s:
    case[i]+=1

ans=sorted([(-cnt,spell) for spell,cnt in case.items()])
idx=0
while idx<26 and ans[idx][0]==ans[0][0]:
    print(ans[idx][1],end='')
    idx+=1
