#include <stdio.h>
#include <string.h>

struct me
{
	char name[7];
};

int main()
{
	struct me myname;
	strcpy(&myname.name, "���ϱ�");
	printf("Hello! Your name is %s\n", myname.name);
	return 0;
}