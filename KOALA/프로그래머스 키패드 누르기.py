numbers=[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand="right"

def solution(numbers,hand):
    pass

if True:
    keypad={(i+1)%11:(i%3,i//3) for i in range(11) if i!=9}
    lefthand=0,3
    righthand=2,3
    ans=''
    handtype='R' if hand=='right' else 'L'
    for i in numbers:
        nowlocate=keypad[i]
        l_dist=abs(nowlocate[0]-lefthand[0])+abs(nowlocate[1]-lefthand[1])
        r_dist=abs(nowlocate[0]-righthand[0])+abs(nowlocate[1]-righthand[1])
        if nowlocate[0]==0:
            ans+='L'
            lefthand=nowlocate
        elif nowlocate[0]==2:
            ans+='R'
            righthand=nowlocate
        else:
            if l_dist<r_dist:
                ans+='L'
                lefthand=nowlocate
            elif l_dist>r_dist:
                ans+='R'
                righthand=nowlocate
            else:
                if handtype=='R':
                    righthand=nowlocate
                else:
                    lefthand=nowlocate
                ans+=handtype
    return ans
