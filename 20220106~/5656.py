from sys import stdin
input=stdin.readline

i=1

while True:
    try:
        if eval(input().rstrip()):
            print(f'Case {i}: true')
        else:
            print(f'Case {i}: false')
        i+=1
    except:
        break
