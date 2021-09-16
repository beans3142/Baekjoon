#include <iostream>
#include <cstdio>
#include <cstring>

#define MAX 1010
#define MOD 10007

using namespace std;

long long dp[MAX][MAX];
char ch[MAX];

int main()
{
    int len, left, right;
    scanf("%s", ch);

    len = strlen(ch);

    for (int i = 0; i < len; i++)
    {
        // a ���� ���
        dp[i][i] = 1;

        // aa ���� ���
        if (ch[i] == ch[i + 1])
            dp[i][i + 1] = 3;

        // ab ���� ���
        else
            dp[i][i + 1] = 2;
    }

    // L�� ���̸� �ǹ��Ѵ�.
    for (int L = 2; L < len; L++)
    {
        for (left = 0; left < len; left++)
        {
            right = left + L;

            if (right > len)
                break;

            dp[left][right] = dp[left + 1][right] + dp[left][right - 1] - dp[left + 1][right - 1] + MOD;

            if (ch[left] == ch[right])
                dp[left][right] += dp[left + 1][right - 1] + 1;

            dp[left][right] %= MOD;
        }
    }

    printf("%lld\n", dp[0][len - 1]);

    return 0;
}