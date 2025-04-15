from sys import stdin
input=stdin.readline

def get(n):
    if n==0:
        return "-"
    line=get(n-1)
    return line+' '*len(line)+line

while True:
    try:
        print(get(int(input())))
    except:
        break
