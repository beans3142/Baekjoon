n=int(input())
ans=input()
sang='ABC'*40
chang='BABC'*25
hyun='CCAABB'*20
score=[0,0,0]
for i in range(n):
    if sang[i]==ans[i]:
        score[0]+=1
    if chang[i]==ans[i]:
        score[1]+=1
    if hyun[i]==ans[i]:
        score[2]+=1

mx=max(score)

print(mx)
if mx==score[0]:
    print('Adrian')
if mx==score[1]:
    print('Bruno')
if mx==score[2]:
    print('Goran')
    
