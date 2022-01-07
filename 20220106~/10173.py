from sys import stdin
input=stdin.readline

while True:
    s=input().rstrip()
    if s=="EOI":
        break
    s=s.lower()
    if s.count("nemo"):
        print("Found")
    else:
        print("Missing")
