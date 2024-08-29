#include <stdio.h>

int main()
{
		int a = 0;
		printf ("this is a gcov test\n");
		if ( a == 0 )
				printf ("branch test a == 0\n") ;
		else
				printf ("branch test a != 0\n") ;
		return (0);
}
