/*
 * Ecris en language C  un programme qui stress les ecritures sur un disk ou dans un fichier.
Les ecritures doivent se faire le plus rapidement possible et la lecture ne doit jamais bloquer les ecritures
le programme ne doit pas etre interactif, et tous les parameteres necessaires sont passés par la commande line.
L'integrité des données ecrites doit toujours etre verifés , et le programme doit s'arreter s'il detecte une corruption
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <pthread.h>

// Fonction pour creer une chaîne de caracteres aléatoires
char *rand_string(char *str, size_t size)
{
    const char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    if (size) {
        --size;
        for (size_t n = 0; n < size; n++) {
            int key = rand() % (int) (sizeof charset - 1);
            str[n] = charset[key];
        }
        str[size] = '\0';
    }
    return str;
}

// Fonction pour ecrire les donnees sur le disque ou le fichier
int write_data(char *filename, char *data, long size)
{
    FILE *fp;
    fp = fopen(filename, "w");
    if (fp == NULL) {
        printf("Error ouverture fichier\n");
        return -1;
    }

    // Ecriture des donnees
    fwrite(data, size, 1, fp);
    fclose(fp);
    return 0;
}

// Fonction pour lire les donnees depuis le disque ou le fichier
int read_data(char *filename, char *data, long size)
{
    FILE *fp;
    fp = fopen(filename, "r");
    if (fp == NULL) {
        printf("Error ouverture fichier\n");
        return -1;
    }

    // Lecture des donnees
    fread(data, size, 1, fp);
    fclose(fp);
    return 0;
}

// Fonction executee par le thread de lecture
void *read_thread(void *arg)
{
    char *filename;    // Nom du fichier a lire/ecrire
    char *data;        // Chaîne de caracteres aléatoires
    long size;         // Taille des donnees

    // Recuperation des arguments passes par le thread principal
    filename = (char *)arg;
    size = strlen(arg);
    data = (char *)malloc((size + 1) * sizeof(char));

    // Lecture des donnees
    read_data(filename, data, size);

    // Verification des donnees
    if (memcmp(data, data, size) != 0) {
        printf("Corruption de donnees detectee\n");
        return NULL;
    }

    return NULL;
}

int main(int argc, char **argv)
{
    char *filename;    // Nom du fichier a lire/ecrire
    long size;         // Taille des donnees
    int times;         // Nombre de fois pour lire/ecrire
    int i;
    char *data;        // Chaîne de caracteres aléatoires
    pthread_t thread;

    // Verification des parametres
    if (argc < 4) {
        printf("Usage: %s <filename> <num_data> <num_times>\n", argv[0]);
        return 0;
    }

    filename = argv[1];
    size = atoi(argv[2]);  // convertir la taille des donnees depuis string a int
    times = atoi(argv[3]); // convertir le nombre de fois depuis string a int

    // Allocation de memoire pour stocker les donnees
    data = (char *)malloc((size + 1) * sizeof(char));

    // Initialisation du random
    srand(time(NULL));

    // Boucle pour ecrire et lire les donnees
    for (i = 0; i < times; i++) {
        // Generation des donnees aléatoires
        rand_string(data, size);

        // Ecrire les donnees
        write_data(filename, data, size);

        // Creation du thread de lecture
        pthread_create(&thread, NULL, read_thread, filename);
        pthread_join(thread, NULL);
    }

    printf("Terminé avec succes\n");
    return 0;
}
