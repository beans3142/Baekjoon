import sys
str = sys.stdin.readline().rstrip()
s = input()
answer = len(str)
caps = False
for i in range(len(str)):
    st = str[i]
    upper = st.isupper()
    if(upper and not caps):
        caps = True
        answer += 1
        if (i < len(str) - 1):
            if (str[i + 1].islower()):  # 대문자가 연속적이지 않은 경우
                caps = False

    elif(caps and not upper): #대문자 -> 소문자
        answer += 1
        caps = False
        if(i < len(str)-1):
            if(str[i+1].isupper()): # 소문자가 연속적이지 않은 경우 (마름모)
                caps = True
print(answer)
