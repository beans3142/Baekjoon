#include <stdio.h>
int main()
{
    int input;
    //red, green, blue ���� ����
    unsigned char red;
    unsigned char green;
    unsigned char blue;
    unsigned int rgb;

    //red ���� input���� �Է¹ް�, �� ��ȯ�� ���� red ������ ����
    scanf("%d", &input);
    red = (unsigned char)input;

    //green ���� input���� �Է¹ް�, �� ��ȯ�� ���� green ������ ����
    scanf("%d", &input);
    green = (unsigned char)input;
    //blue ���� input���� �Է¹ް�, �� ��ȯ�� ���� blue ������ ����
    scanf("%d", &input);
    blue = (unsigned char)input;

    rgb = red | (green << 8) | (blue << 16);
    printf("RGB Ʈ���÷�: %06x \n", rgb);

    return 0;
}