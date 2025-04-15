from sys import stdin
input = stdin.readline

def check_nnn(n, s):
    cnt = [0] * n
    for ch in s:
        cnt[int(ch, 36)] += 1
    for i in range(n):
        if cnt[i] != int(s[i], 36):
            return False
    return True

def generate_nnn(n):
    max_num = n ** n
    valid_numbers = []
    
    for i in range(max_num):
        num_str = ""
        temp = i
        for _ in range(n):
            num_str = chr((temp % n) + (48 if temp % n < 10 else 55)) + num_str
            temp //= n
        
        if check_nnn(n, num_str):
            valid_numbers.append(num_str)
    
    return valid_numbers

n = int(input().strip())

result = generate_nnn(n)
if result:
    print("\n".join(result))
else:
    print("EI OLE")
