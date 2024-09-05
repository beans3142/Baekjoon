for _ in range(int(input())):
    n=int(input())
    arr=sorted(map(int,input().split()))
    st=[]
    for i in arr:
        if st and st[-1]==i:
            st.pop()
        else:
            st.append(i)
    print(f'Case #{i+1}:',st[0])