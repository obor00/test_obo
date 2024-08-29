#include <string.h>
#include <stdio.h>

int main()
{
	printf ("result=%s len=%d\n", strstr ("abcdefg","efg"), strlen(strstr ("abcdefg","efg")));
	printf ("result=%s\n", strstr ("abcdefg","cde"));


}
