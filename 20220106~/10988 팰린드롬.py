word=input()
for i in range(len(word)//2+1):
    if word[i] != word[-1-i]:
        print(0)
        break
    elif i==len(word)//2:
        print(1)
        break
    
#https://www.acmicpc.net/problem/10988
'''
word = list(str(input()))

if list(reversed(word)) == word:
    print(1)
else:
    print(0)
'''
# 차선책, 스크랩해온것?;
