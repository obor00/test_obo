#include <dirent.h>

int main ()
{
  struct dirent mystruct;

  DIR * mydir= opendir("toto");
  int v = readdir (mydir);
}
