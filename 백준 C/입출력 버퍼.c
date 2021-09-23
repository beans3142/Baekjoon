#include <stdio.h>

int main()
{
	char s1[100];

	char s2[100];

	char s3[100];

	printf("값 입력 : ");

	gets(s1);

	printf("\ngets() 를 통해 입력받은 값 : %s\n\n", s1);

	printf("값 입력 : ");

	scanf("%[^\n]s", s2);

	printf("\nscanf([^\\n]) 를 이용해 입력받은 값 : %s\n\n", s2);

	printf("값 입력 : ");

	scanf("%s", s3);

	printf("\nscanf() 를 이용해 입력받은 값 : %s\n\n", s3);
}