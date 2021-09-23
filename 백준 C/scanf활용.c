#include <stdio.h>

int main()
{
	int a = 1234567;
	char s[6] = { 'h','e','l','l','o','\0'};
	printf("%05d\n", a);
	printf("%7s\n", s);
}