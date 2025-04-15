d={}
for w in sorted([input() for _ in[0]*(int(input()))],key=lambda x:-len(x)):
    t=1
    for W in d:
        if w==W[:len(w)]:
            t=0
            break
    if t:d[w]=1
print(len(d))
