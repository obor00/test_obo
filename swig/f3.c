// example string returned
#include <stdio.h>

char name0[32];

int f3 (char *name)
{
	sprintf (name,"Hello");
	return 1;
}

int f3b (char *name)
{
	sprintf (name,"again");
	return 1;
}

int main()
{
	f3(name0);
	printf ("result=%s\n", name0);
}
