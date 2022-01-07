from sys import stdin
input=stdin.readline

alphabet={chr(97+i):0 for i in range(26)}
word=input().rstrip()
for i in word:
    alphabet[i]+=1

print(*list(alphabet.values()))
