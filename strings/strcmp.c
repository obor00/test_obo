#include <string.h>
#include <stdio.h>

int main()
{
	printf ("result=%d\n", strcmp("1234","12345"));
	int v=strcmp("1234","1234");
	printf ("result=%d\n", v);
	if (v)
		printf ("true\n");
	else
		printf ("false\n");
	printf ("result=%d\n", strcmp("12345","1234"));
}
