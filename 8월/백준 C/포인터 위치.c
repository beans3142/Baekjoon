#include <stdio.h>

int main(void)
{

    //char ch = 'A';
    //char* p;
    //char* q; // <- �������� ����?
    //p = &ch;
    //q = *p; // 'A' ���ڿ��� + - ���ڰ��� ���������� �̿��Ϸ��� �ƽ�Ű�ڵ尪 00000041
    //*q = 'Z'; // �ƽ�Ű �ڵ尪�� �����


    //printf("ch�� ������ �ִ� �� : ch -> %c \n\n", ch);

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