#include <stdio.h>
#include <string.h>

int main()
{
    char arr[1000000];
    int cnt = 0;
    int i = 0;
    int len;
    scanf("%[^\n]", arr);
    len = strlen(arr);

    if (len == 1)
    {
        if (arr[i] == ' ')
        {
            printf("0");
            return 0;

        }
    }
    if (arr[len - 1] == ' ')
    {
        cnt -= 1;
    }
    for (int i = 1; i <= len; i++)
    {
        if (arr[i] == ' ')
        {
            cnt++;
        }
    }
    printf("%d", cnt + 1);



}