#include <stdio.h>

int main()
{
	char s1[100];

	char s2[100];

	char s3[100];

	printf("�� �Է� : ");

	gets(s1);

	printf("\ngets() �� ���� �Է¹��� �� : %s\n\n", s1);

	printf("�� �Է� : ");

	scanf("%[^\n]s", s2);

	printf("\nscanf([^\\n]) �� �̿��� �Է¹��� �� : %s\n\n", s2);

	printf("�� �Է� : ");

	scanf("%s", s3);

	printf("\nscanf() �� �̿��� �Է¹��� �� : %s\n\n", s3);
}