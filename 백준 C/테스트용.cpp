#include <stdio.h>
int main()
{
    int input;
    //red, green, blue 변수 선언
    unsigned char red;
    unsigned char green;
    unsigned char blue;
    unsigned int rgb;

    //red 값을 input으로 입력받고, 형 변환을 통해 red 변수에 저장
    scanf("%d", &input);
    red = (unsigned char)input;

    //green 값을 input으로 입력받고, 형 변환을 통해 green 변수에 저장
    scanf("%d", &input);
    green = (unsigned char)input;
    //blue 값을 input으로 입력받고, 형 변환을 통해 blue 변수에 저장
    scanf("%d", &input);
    blue = (unsigned char)input;

    rgb = red | (green << 8) | (blue << 16);
    printf("RGB 트루컬러: %06x \n", rgb);

    return 0;
}