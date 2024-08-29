#include <stdio.h>

int main()
{
	int v0 = 0;
	int v1 = 1;

	printf ("v0=%d, v1=%d\n",v0,v1);
	if (v0)
		printf ("if(v0) is true\n");
	else
		printf ("if(v0) is false\n");

	if (v1)
		printf ("if (v1) is true\n");
	else
		printf ("if (v1) is false\n");

	if (!v0)
		printf ("if (!v0) is true\n");
	else
		printf ("if (!v0) is false\n");
	if (!v1)
		printf ("if (!v1) is true\n");
	else
		printf ("if (!v1) is false\n");
}
