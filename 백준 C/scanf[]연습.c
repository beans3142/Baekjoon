#include <stdio.h>

int main() {
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);
	printf("%02d-%03d-%04d", a, abs(b), abs(c));
	return 0;
}