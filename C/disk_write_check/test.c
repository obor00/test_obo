#include <stdio.h>
#include <string.h>

int main(void) {

   FILE *f;
   char chaine[10];
   int i;

   //Ecriture des 100 caracteres
   f = fopen("toto.txt", "w+");
   for (i = 0; i < 10; i++) {
      chaine[i] = 'a'+ i;
   }
   fputs(chaine, f);

   //Relis les caracteres
   fseek(f, 3, SEEK_SET);
   fread(chaine,1, 3, f);
   chaine[4] = 0;
   printf("Les caracteres 5 a 8 sont: %s \n", chaine);

   //Ecriture des 100 autres caracteres
   fseek(f, 0, SEEK_END); //
   for (i = 0; i < 10; i++) {
      chaine[i] = 'A' + i;
   }
   fputs(chaine, f);

   fclose(f);
   return 0;
}
