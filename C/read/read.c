#include <stdio.h>

#define SIZE 256

int main (int argc, char *argv[])
{
	char buf[SIZE];
	int i;
	int fd= open (argv[1], 0);

	for (i=0; i< SIZE; i++)
		buf[i] = 'a';
	int r = read (fd, buf, SIZE);

	printf ("file %s, fd=%d, size read=%d, %s\n", argv[1], fd, r, buf);
	return 0;
}
