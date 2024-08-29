/*
Ecris un programme en C sous linux qui ecris des blocs de données, relis ces blocs un par un et verifie que l'integristé des données par sha1sum
Voila les parametres a passer en ligne de commande:
- nom du fichier a ouvrir
- taille d'un bloc a ecrire
- taille maximum du fichier
- temps maximum d'execution du programme en secondes
Details d'implementation:
- l'ecriture d'un bloc se fait avec des données aleatoires
- tous les blocs ecrits doivent etre verifiés par une relecture et leur md5sum ou SHA1 doit etre juste
- l'ecriture des blocs est asynchrone
- la lecture des blocs est asynchrone
- utilise un file descripteur et non pas un file pointer(fp)
utilise un thread pour la lecture et l'ecriture?
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/time.h>
#include <sys/wait.h>
#include <pthread.h>
#include <openssl/sha.h>

#define MAX_FILENAME_LEN 128
#define MAX_FILE_SIZE (1<<30) //1Go
#define MAX_BLOCK_SIZE (1<<20) //1 Mo
#define MAX_EXEC_TIME 10 //10 secondes

//Structure pour passer les parametres aux threads
typedef struct {
    int fd;
    int blockSize;
    unsigned char *data;
    unsigned char *hash;
    off_t offset;
} ThreadData;

//Fonction pour générer des données aléatoires
void fillRandomData(unsigned char *data, int dataLen) {
    for (int i = 0; i < dataLen; i++) {
        data[i] = 48 + rand() % (122-48);
    }
}

//Fonction pour calculer le hash SHA1 des données
void computeHash(unsigned char *data, int dataLen, unsigned char *hash) {
    SHA1(data, dataLen, hash);
}

//Fonction pour le thread d'ecriture
void *writeThread(void *arg) {
    //Recuperer les donnees du thread
    ThreadData *data = (ThreadData*)arg;

    //Ecriture asynchrone
    int ret = pwrite(data->fd, data->data, data->blockSize, data->offset);
    if (ret != data->blockSize) {
        fprintf(stderr, "Error : write failed\n");
        return NULL;
    }

    return NULL;
}

//Fonction pour le thread de lecture
void *readThread(void *arg) {
    //Recuperer les donnees du thread
    ThreadData *data = (ThreadData*)arg;

    //Lecture asynchrone
    int ret = pread(data->fd, data->data, data->blockSize, data->offset);
    if (ret != data->blockSize) {
        fprintf(stderr, "Error : read failed\n");
        return NULL;
    }

    //Recalculer le hash
    unsigned char newHash[SHA_DIGEST_LENGTH];
    computeHash(data->data, data->blockSize, newHash);

    //Verifier l'integrite des donnees
    if (memcmp(data->hash, newHash, SHA_DIGEST_LENGTH) != 0) {
        fprintf(stderr, "Error : data integrity check failed\n");
        return NULL;
    }

    return NULL;
}

//Fonction principal
int main(int argc, char *argv[]) {
    //Verifier que les parametres sont corrects
    if (argc < 5) {
        fprintf(stderr, "Usage : %s <filename> <block_size> <max_file_size> <max_exec_time>\n", argv[0]);
        return -1;
    }

    //Recuperer les parametres
    char filename[MAX_FILENAME_LEN];
    strcpy(filename, argv[1]);
    int blockSize = atoi(argv[2]);
    int maxFileSize = atoi(argv[3]);
    int maxExecTime = atoi(argv[4]);

    //Verifier les parametres
    if (blockSize > MAX_BLOCK_SIZE || maxFileSize > MAX_FILE_SIZE || maxExecTime > MAX_EXEC_TIME) {
        fprintf(stderr, "Error : invalid parameters\n");
        return -1;
    }

    //Creer le fichier
    int fd = open(filename, O_APPEND | O_CREAT);
    if (fd == -1) {
        fprintf(stderr, "Error : unable to create file\n");
        return -1;
    }

    //Calculer le temps maximum d'execution
    struct timeval startTime;
    struct timeval endTime;
    gettimeofday(&startTime, NULL);
    gettimeofday(&endTime, NULL);
    int execTime = (endTime.tv_sec - startTime.tv_sec) + (endTime.tv_usec - startTime.tv_usec) / 1000000;

    //Allouer la memoire pour le bloc de donnees
    unsigned char *data = (unsigned char *)malloc(blockSize);
    if (data == NULL) {
        fprintf(stderr, "Error : unable to allocate memory\n");
        return -1;
    }

    //Creer les threads
    pthread_t writeThreadId;
    pthread_t readThreadId;
    ThreadData threadData;
    threadData.fd = fd;
    threadData.blockSize = blockSize;
    threadData.data = data;
    threadData.hash = malloc(SHA_DIGEST_LENGTH);
    threadData.offset = 0;

    //Boucle principale
    int writtenBytes = 0;
    while (execTime < maxExecTime && writtenBytes < maxFileSize) {
        //Generer des donnees aleatoires
        fillRandomData(data, blockSize);

        //Calculer le hash
        computeHash(data, blockSize, threadData.hash);

        //Lancer le thread d'ecriture
        pthread_create(&writeThreadId, NULL, writeThread, &threadData);

        //Lancer le thread de lecture
        pthread_create(&readThreadId, NULL, readThread, &threadData);

        //Attendre que le thread d'ecriture se termine
        pthread_join(writeThreadId, NULL);

        //Attendre que le thread de lecture se termine
        pthread_join(readThreadId, NULL);

        //Mettre a jour le temps d'execution
        gettimeofday(&endTime, NULL);
        execTime = (endTime.tv_sec - startTime.tv_sec) + (endTime.tv_usec - startTime.tv_usec) / 1000000;

        //Mettre a jour l'offset
        threadData.offset += blockSize;
        writtenBytes += blockSize;
    }

    //Fermer le fichier
    close(fd);

    //Liberer la memoire
    free(threadData.hash);
    free(data);

    return 0;
}

