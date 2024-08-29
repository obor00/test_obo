/* Ecris un programme en C sous linux qui effectue les actions suivantes:

ouvre un fichier de type device
ecris des blocs de données
en parallele de l'ecriture, relis les données et verifie que ce qui est relis est egal a ce qui a eté ecris

parametres:
  - nom du fichier
 - taille max du fichier
 - taille des blocs a ecrire
 - nombre de secondes

la lecture doit se faire en parallele a l'ecriture (ecriture asynchrone)
quand la taille max du fichier est atteinte, recommence au debut
boucle a l'infini pendant nombre de secondes
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <pthread.h>

//parametres
char *filename;
int max_file_size;
int block_size;
int num_seconds;

//variables globales
int fd;
int bytes_written;
int bytes_read;

//fonctions
void *read_data(void *param);

int main(int argc, char *argv[])
{
    if(argc != 5) {
        printf("Usage: %s <filename> <max_file_size> <block_size> <num_seconds>\n", argv[0]);
        exit(1);
    }

    filename = argv[1];
    max_file_size = atoi(argv[2]);
    block_size = atoi(argv[3]);
    num_seconds = atoi(argv[4]);

    //ouvrir le fichier
    fd = open(filename, O_RDWR | O_CREAT, 0666);
    if(fd < 0) {
        perror("open");
        exit(1);
    }

    //creer un thread pour la lecture
    pthread_t read_thread;
    int ret = pthread_create(&read_thread, NULL, read_data, NULL);
    if(ret < 0) {
        perror("pthread_create");
        exit(1);
    }

    //ecrire des donnees
    int i = 0;
    char *buf = (char *) malloc(block_size);
    memset(buf, 'A' + i, block_size);
    while(1) {
        bytes_written = write(fd, buf, block_size);
        if(bytes_written < 0) {
            perror("write");
            exit(1);
        }
        i = (i + 1) % 26;
        memset(buf, 'A' + i, block_size);
        //verifier si on a atteint la taille max du fichier
        if(lseek(fd, 0, SEEK_CUR) == max_file_size) {
            //retourner au debut du fichier
            lseek(fd, 0, SEEK_SET);
        }
        //arret apres num_seconds
        if(num_seconds <= 0) {
            break;
        }
    }

    //attendre que le thread de lecture se termine
    pthread_join(read_thread, NULL);

    //fermer le fichier
    close(fd);

    return 0;
}

void *read_data(void *param)
{
    //lire les donnees
    char *buf = (char *) malloc(block_size);
	while(1) {
			bytes_read = read(fd, buf, block_size);
			if(bytes_read < 0) {
					perror("read");
					exit(1);
			}
			//verifier si ce qui a ete lu est egal a ce qui a ete ecrit
			if(memcmp(buf, "A", block_size) != 0) {
					perror("data mismatch");
					exit(1);
			}
			// fin du test
			clock_gettime(CLOCK_MONOTONIC, &end);
			if(end.tv_sec - start.tv_sec >= num_seconds) {
					break;
			}
	}

	return NULL;
}
