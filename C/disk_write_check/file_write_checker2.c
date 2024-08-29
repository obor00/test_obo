/* Ecris un programme en C sous linux qui effectue les actions suivantes:

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

#define MAX_FILE_SIZE 1024
#define MAX_BLOCK_SIZE 512

void *writeData(void *arg);
void *readData(void *arg);

//Struct pour les parametres
typedef struct params{
    FILE *fp;
    int max_file_size;
    int max_block_size;
    int max_exec_time;
} params;

int main(){
    FILE *fp;
    int max_file_size;
    int max_block_size;
    int max_exec_time;
    pthread_t writeThread, readThread;
    params *parameters;

    //Ouvrir le fichier et le creer s'il n'existe pas
    fp = fopen("data.txt", "a+");

    //Demander l'utilisateur de rentrer les parametres
    printf("Entrez la taille maximale du fichier: ");
    scanf("%d", &max_file_size);
    printf("Entrez la taille d'un bloc: ");
    scanf("%d", &max_block_size);
    printf("Entrez le temps d'execution maximum du programme: ");
    scanf("%d", &max_exec_time);

    //Creer les parametres
    parameters = malloc(sizeof(params));
    parameters->fp = fp;
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
    fclose(fp);

    return 0;
}

//Fonction pour le thread d'ecriture
void *writeData(void *arg){
    params *parameters = (params *)arg;
    FILE *fp = parameters->fp;
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
            rewind(fp);
        }

        //Ecriture des donnees
        fwrite(data, sizeof(char), max_block_size, fp);
        file_size += max_block_size;
    }

    return NULL;
}

//Fonction pour le thread de relecture
void *readData(void *arg){
    params *parameters = (params *)arg;
    FILE *fp = parameters->fp;
    int max_block_size = parameters->max_block_size;
    char data[max_block_size];

    //Lire le fichier et verifier le contenu
    while(fread(data, sizeof(char), max_block_size, fp)){
        for(int i = 0; i < max_block_size; i++){
            if(data[i] < 'A' || data[i] > 'Z'){
                printf("Erreur de relecture\n");
            }
        }
    }

    return NULL;
}
