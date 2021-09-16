from sys import stdin
input=stdin.readline

k=int(input())
arr=['4','7']
lower=0
add=2
mx=0
while lower<k:
    mx+=1
    lower+=add
    add*=2
left=1+k-lower//2

bit_ans=bin(2**mx-left)[2:]
while len(bit_ans)<mx:
    bit_ans='0'+bit_ans

for i in range(len(bit_ans)):
    print(4 if bit_ans[i]!='0' else 7,end='')
