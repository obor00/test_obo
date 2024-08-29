/*
 * Ecris un programme en C sous linux qui effectue les actions suivantes:

ouvre un fichier, et  crée le seulement s'il nexiste pas
Ecris des blocs de donées aleatoires aussi vite que possible.
la taille d'un bloc est configurable
La taille maximum du fichier est configurable
Si le fichier depasse sa taille maximum, alors recommence a ecrire les blocs depuis le debut du fichier

Toutes les blocs ecris doivent etre verifiés en parallele par une relecture dans le fichier.
La relecture ne doit jamais  bloquer les ecritures qui doivent continuer aussi vite que possible.

Le temps d'execution maximum du programme doit etre configurable.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <pthread.h>
#include <unistd.h>
#include <fcntl.h>

#define MAX_FILE_SIZE 1024
#define MAX_BLOCK_SIZE 512

void *writeData(void *arg);
void *readData(void *arg);

//Struct pour les parametres
typedef struct params{
    int fd;
    int max_file_size;
    int max_block_size;
    int max_exec_time;
} params;

int main(int argc, char **argv){
    int fd;
    int max_file_size;
    int max_block_size;
    int max_exec_time;
    pthread_t writeThread, readThread;
    params *parameters;

    //Verifier les arguments
    if(argc < 4){
        printf("Usage: ./programme max_file_size max_block_size max_exec_time\n");
        return -1;
    }

    //Ouvrir le fichier et le creer s'il n'existe pas
    fd = open("data.txt", O_RDWR | O_CREAT);

    //Recuperer les parametres
    max_file_size = atoi(argv[1]);
    max_block_size = atoi(argv[2]);
    max_exec_time = atoi(argv[3]);

    //Creer les parametres
    parameters = malloc(sizeof(params));
    parameters->fd = fd;
    parameters->max_file_size = max_file_size;
    parameters->max_block_size = max_block_size;
    parameters->max_exec_time = max_exec_time;

    //Creer le thread d'ecriture
    pthread_create(&writeThread, NULL, writeData, (void *)parameters);

    //Creer le thread de relecture
    pthread_create(&readThread, NULL, readData, (void *)parameters);

    //Attendre que les threads se terminent
    pthread_join(writeThread, NULL);
    pthread_join(readThread, NULL);

    //Fermer le fichier
    close(fd);

    return 0;
}

//Fonction pour le thread d'ecriture
void *writeData(void *arg){
    params *parameters = (params *)arg;
    int fd = parameters->fd;
    int max_file_size = parameters->max_file_size;
    int max_block_size = parameters->max_block_size;
    int max_exec_time = parameters->max_exec_time;
    time_t start_time, cur_time;
    int file_size = 0;
    char data[max_block_size];

    //Recuperer le temps de debut
    time(&start_time);

    //Boucle qui s'execute pendant le temps d'execution maximum
    while(1){
        //Verifier le temps d'execution
        time(&cur_time);
        if(difftime(cur_time, start_time) > max_exec_time){
            break;
        }

        //Generer des donnees aleatoires
        srand(time(NULL));
        for(int i = 0; i < max_block_size; i++){
            data[i] = rand() % 26 + 'A';
        }

        //Verifier la taille du fichier
        if(file_size + max_block_size > max_file_size){
            //Reecrire depuis le debut du fichier
            file_size = 0;
            lseek(fd, 0, SEEK_SET);
        }

        //Ecriture des donnees
        write(fd, data, max_block_size);
        file_size += max_block_size;
    }

    return NULL;
}

//Fonction pour le thread de relecture
void *readData(void *arg){
    params *parameters = (params *)arg;
    int fd = parameters->fd;
    int max_block_size = parameters->max_block_size;
    char data[max_block_size];

    //Lire le fichier et verifier le contenu
    while(read(fd, data, max_block_size)){
        for(int i = 0; i < max_block_size; i++){
            if(data[i] < 'A' || data[i] > 'Z'){
                printf("Erreur de relecture\n");
            }
        }
    }

    return NULL;
}
