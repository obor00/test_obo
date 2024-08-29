/*
 * Ecris un programme en C sous linux qui effectue les actions suivantes:

Parametres passés en ligne de commande:
- nom du fichier a ouvrir
- taille d'un bloc a ecrire
- taille maximum du fichier
- temps maximum d'execution du programme en secondes

Objectif:
  Verifier l'integrité des données d'un fichier

Specifications:
- l'ecriture d'un bloc se fait avec des données aleatoires
  le md5sum ou le sha1 du bloc est conservé
- si le fichier depasse la taille maximum alors l'ecriture doit recommencer au debut du fichier
- tous les blocs ecrits doivent etre verifiés par une relecture et leur md5sum ou SHA1 doit etre juste
- l'ecriture des blocs doit se faire aussi vite que possible sans attente
- la lecture doit se faire en parallele des ecritures par un thread
- la relecture des blocs ne doit pas perturber ni bloquer l'ecriture
- utilise un file descripteur et non pas un file pointer(fp)
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <pthread.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <sys/time.h>
#include <openssl/md5.h>
#include <openssl/sha.h>

// Definition des variables globales
int fd;
int BLOCKSIZE = 10;
int maxSize;
int timeMax;
int wait = 1;
int rand_i = 0;
int stop = 0;

// Fonction pour générer des données aléatoires
void randomize(char* buf, int size) {
  // for (i = 0; i < size; i++) {
  //   buf[i] = rand() % 256;
  // }
  memset(buf, 'A' + rand_i++, size);
}

// Fonction pour calculer le MD5/SHA1
void calcHash(char* buf, int size, char* hash) {
  int i;
  unsigned char md5sum[MD5_DIGEST_LENGTH];
  unsigned char sha1sum[SHA_DIGEST_LENGTH];

  MD5(buf, size, md5sum);
  SHA1(buf, size, sha1sum);

  for (i = 0; i < MD5_DIGEST_LENGTH; i++) {
    sprintf(&hash[i*2], "%02x", md5sum[i]);
  }

  for (i = 0; i < SHA_DIGEST_LENGTH; i++) {
    sprintf(&hash[(i+16)*2], "%02x", sha1sum[i]);
  }
}

// Fonction pour lire un bloc et verifier son intégrité
void *readBlock(void *arg) {
  // int offset = *((int *) arg);
  char buf[BLOCKSIZE];
  char hash[MD5_DIGEST_LENGTH + SHA_DIGEST_LENGTH];
  char hash2[MD5_DIGEST_LENGTH + SHA_DIGEST_LENGTH];

	while (1)
	{
		if (stop == 1)
			break;
		if (wait == 1)
			continue;

		//lseek(fd, offset, SEEK_SET);
		read(fd, buf, BLOCKSIZE);

		calcHash(buf, BLOCKSIZE, hash);

		//lseek(fd, offset + BLOCKSIZE, SEEK_SET);
		read(fd, hash2, MD5_DIGEST_LENGTH + SHA_DIGEST_LENGTH);

		if (strcmp(hash, hash2) != 0) {
			printf("Error: Block corrupted %s , hash %s\n", buf, hash2);
		}
		else
			printf("OK: block %s \n", buf);
	}
  pthread_exit(NULL);
}

int main(int argc, char *argv[]) {
  int offset = 0;
  char buf[BLOCKSIZE];
  char hash[MD5_DIGEST_LENGTH + SHA_DIGEST_LENGTH];
  struct timeval start, end;
  pthread_t thread;

  // Vérifier les paramètres
  if (argc != 4) {
    printf("Usage: %s <filename> <maxSize> <timeMax>\n", argv[0]);
    exit(1);
  }
  maxSize = atoi(argv[2]);
  timeMax = atoi(argv[3]);

  // Ouvrir le fichier
  fd = open(argv[1], O_RDWR | O_CREAT, 0644);
  if (fd == -1) {
    perror("Error opening file");
    exit(1);
  }

	pthread_create(&thread, NULL, readBlock, NULL);
	// Calculer le temps d'execution
  gettimeofday(&start, NULL);
  while (1) {
    randomize(buf, BLOCKSIZE);
    calcHash(buf, BLOCKSIZE, hash);
    write(fd, buf, BLOCKSIZE);
    write(fd, hash, MD5_DIGEST_LENGTH + SHA_DIGEST_LENGTH);
    offset += BLOCKSIZE;
    if (offset >= maxSize) {
      offset = 0;
    }
    gettimeofday(&end, NULL);
    if ((end.tv_sec - start.tv_sec) >= timeMax) {
			stop = 1;
      break;
    }
		wait = 0;
  }

  pthread_join(thread, NULL);

  // Fermer le fichier
  close(fd);

  return 0;
}
