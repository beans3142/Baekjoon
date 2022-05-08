from sys import stdin,setrecursionlimit
setrecursionlimit(100000)
input=stdin.readline


case={"h", "b", "c", "n", "o", "f", "p", "s", "k", "v", "y", "i","w", "u","ba", "ca" , 
"ga", "la", "na", "pa", "ra", "ta", "db", "nb", "pb", "rb", "sb", "tb", "yb", "ac",
"sc", "tc", "cd", "gd", "md", "nd", "pd", "be", "ce", "fe", "ge", "he", "ne", "re", "se", "te",
"xe", "cf", "hf", "rf", "ag", "hg", "mg", "rg", "sg", "bh", "rh", "th", "bi", "li", "ni", "si",
"ti", "bk", "al", "cl", "fl", "tl", "am", "cm", "fm", "pm", "sm", "tm", "cn", "in", "mn", "rn",
"sn", "zn", "co", "ho", "mo", "no", "po", "np", "ar", "br", "cr", "er", "fr", "ir", "kr", "lr",
"pr", "sr", "zr", "as", "cs", "ds", "es", "hs", "os", "at", "mt", "pt", "au", "cu", "eu", "lu",
"pu", "ru", "lv", "dy"}

def bt(idx):
    global able
    if idx==le:
        able=True
        return
    if idx<le:
        if s[idx] in case and vi[idx+1]==0:
            bt(idx+1)
            vi[idx+1]=True
        if s[idx]+s[idx+1] in case and vi[idx+2]==0:
            vi[idx+2]=True
            bt(idx+2)
    

for i in range(int(input())):
    s=input()
    le=len(s)-1
    able=False
    vi=[0]*(le+2)
    bt(0)
    if able:
        print('YES')
    else:
        print('NO')
