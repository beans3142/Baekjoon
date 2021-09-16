#include <stdio.h>

int main(void)
{

    //char ch = 'A';
    //char* p;
    //char* q; // <- 포인터형 변수?
    //p = &ch;
    //q = *p; // 'A' 문자에서 + - 문자값을 정수형으로 이용하려면 아스키코드값 00000041
    //*q = 'Z'; // 아스키 코드값이 저장됨


    //printf("ch가 가지고 있는 값 : ch -> %c \n\n", ch);

    /*int* a;
    int pa = 5;
    a = &pa;
    a = 123;
    printf("%d", 123);*/

    int arr[3];
    printf("%p\n", &arr);
    printf("%p\n", &arr[0]);
    printf("%p\n", &arr[1]);
    printf("%p\n", &arr[2]);


    return 0;
}