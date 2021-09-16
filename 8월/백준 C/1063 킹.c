#include <stdio.h>
#include <string.h>

int main()
{
    char k[3];
    char s[3];
    int n;
    scanf("%s %s %d", k, s, &n);

    int kx = k[0] - 'A';
    int ky = k[1] - '0';

    //printf("%d %d", kx, ky);

    int sx = s[0] - 'A';
    int sy = s[1] - '0';

    for (int i = 0; i < n; i++)
    {
        char order[3];
        int move[2] = { 0,0 };
        scanf("%s", order);
        int len = strlen(order);

        for (int j = 0; j < len; j++)
        {
            if (order[j] == 'B')
            {
                move[1] = -1;
            }
            else if (order[j] == 'L')
            {
                move[0] = -1;
            }
            else if (order[j] == 'R')
            {
                move[0] = 1;
            }
            else if (order[j]=='T')
            {
                move[1] = 1;
            }
        }
        int nkx = kx + move[0];
        int nky = ky + move[1];
        int nsx = sx;
        int nsy = sy;
        if (nkx == sx && nky == sy)
        {
            nsx = sx + move[0];
            nsy = sy + move[1];
        }
        if (-1 < nkx && nkx < 8 && 0 < nky && nky < 9 && -1 < nsx && nsx < 8 && 0 < nsy && nsy <9)
        {
            kx = nkx;
            ky = nky;
            sx = nsx;
            sy = nsy;
        }
        //printf("%c%d\n", 'A' + ky, kx);
        //printf("%c%d\n", 'A' + sy, sx);
    }
    printf("%c%d\n", 'A' + kx, ky);
    printf("%c%d", 'A' + sx, sy);
    return 0;
}