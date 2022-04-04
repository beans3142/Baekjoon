
for i in range(int(input())):
    a_list=[] ; b_list=[]
    for j in range(int(input())):
        a,b=input().split()
        b=int(b)
        a_list.append(a) ; b_list.append(b)
    print(a_list[b_list.index(max(b_list))])

'''
a=[['a',3],['b',5],['c',7]]
a_list=[]

for i in range(len(a)):
    a_list.append(a[i][1])
'''
