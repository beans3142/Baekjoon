#include <stdio.h>
#include <limits.h>

int main() {
	printf("\n현재 시스템의 C컴파일러의 데이터 유형의 크기와 값의 범위:\n");

	printf("signed char: ");
	printf("%d byte, 범위: %d ~ %d \n", sizeof(char), CHAR_MIN, CHAR_MAX);

	printf("unsigned char: ");
	printf("%d byte, 범위: %d ~ %d \n", sizeof(unsigned char), 0, UCHAR_MAX);

	printf("signed short int: ");
	printf("%d byte, 범위: %d ~ %d \n", sizeof(signed short int), SCHAR_MIN, SCHAR_MAX);

	printf("unsigned short int: ");
	printf("%d byte, 범위: %d ~ %d \n", sizeof(unsigned short int), 0, USHRT_MAX);

	printf("signed int: ");
	printf("%d byte, 범위: %d ~ %d \n", sizeof(int), INT_MIN, INT_MAX);

	printf("unsigned int: ");
	printf("%d byte, 범위: %d ~ %u \n", sizeof(unsigned int), 0, UINT_MAX);

	return 0;
}