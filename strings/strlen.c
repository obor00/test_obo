#include <string.h>
#include <stdio.h>

int main()
{
	int v=strlen(0);

	printf ("result=%d\n", v);
	if (v)
		printf ("true\n");
	else
		printf ("false\n");
	printf ("result=%d\n", strcmp("12345","1234"));
}
