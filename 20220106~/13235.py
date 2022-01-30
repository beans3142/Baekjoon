def is_true(arr):
    able=True
    for i in range(len(arr)//2):
        if arr[i]!=arr[~i]:
            able=False
    return able

s=input()
if is_true(s):
    print('true')
else:
    print('false')
