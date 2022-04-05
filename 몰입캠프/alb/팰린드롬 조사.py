s=input()
able=True
for i in range(len(s)):
    if s[i]!=s[~i]:
        able=False
        break

if able:
    print('YES')
else:
    print('NO')

'''
짝수에도 잘 작동하나 확인
in
ABBA

out
YES

in
AA

out
YES

in
A

out
YES

'''
