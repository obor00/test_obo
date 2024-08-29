/* a l'aide de la stdlib en language C, ecris une librairie qui fournit la gestion de liste c'est a dire:
- creation de liste
- ajout d'un element en debut de liste
- suppresion  d'un element en fin de liste
- recherche d'un element dans la liste
*/
#include <stdio.h>
#include <stdlib.h>

// Structure pour les éléments de la liste
struct Node {
    int data;
    struct Node* next;
};

// Fonction pour créer une liste vide
struct List {
    struct Node* head;
    struct Node* tail;
};

struct List* createList() {
    struct List* list = (struct List*)malloc(sizeof(struct List));
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = NULL
    newNode->next = NULL;
    list->head = newNode;
    list->tail = newNode;
    return list;
}

// Fonction pour ajouter un élément en début de liste
struct List* addToList(struct List* list, int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    if (list->head == NULL) {
        list->head = newNode;
        list->tail = newNode;
    } else {
        newNode->next = list->head;
        list->head = newNode;
    }
    return list;
}

// Fonction pour supprimer un élément en fin de liste
struct List* removeFromList(struct List* list) {
    if (list->head == NULL)
        return NULL;
    else if (list->head == list->tail) {
        free(list->head);
        list->head = NULL;
        list->tail = NULL;
        return list;
    } else {
        struct Node* temp = list->head;
        while (temp->next != list->tail) {
            temp = temp->next;
        }
        free(list->tail);
        list->tail = temp;
        list->tail->next = NULL;
        return list;
    }
}

// Fonction pour rechercher un élément dans la liste
struct Node* searchInList(struct List* list, int data) {
    struct Node* current = list->head;
    while (current != NULL) {
        if (current->data == data)
            return current;
        current = current->next;
    }
    return NULL;
}

// Fonction pour créer une liste vide
struct Node* createList() {
    return NULL;
}

// Fonction pour ajouter un élément en début de liste
struct Node* addToList(struct Node* head, int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = head;
    head = newNode;
    return head;
}

// Fonction pour supprimer un élément en fin de liste
struct Node* removeFromList(struct Node* head) {
    struct Node* temp = head;
    head = head->next;
    free(temp);
    return head;
}

// Fonction pour rechercher un élément dans la liste
struct Node* searchInList(struct Node* head, int data) {
    struct Node* current = head;
    while (current != NULL) {
        if (current->data == data)
            return current;
        current = current->next;
    }
    return NULL;
}


int main(void) {
    // Création d'une liste
    struct Node* head = createList();

    // Ajout d'un élément
    head = addToList(head, 10);
    head = addToList(head, 20);
    head = addToList(head, 30);
    head = addToList(head, 40);

    // Recherche d'un élément
    struct Node* result = searchInList(head, 20);
    if (result != NULL)
        printf("Element trouvé: %d\n", result->data);
    else
        printf("Element inexistant\n");

	struct Node * node = head;
	while (node != NULL)
	{
        printf("Element : %d\n", node->data);
		node = node -> next;
	}
    // Suppression d'un élément
    head = removeFromList(head);
	printf("Element supprimé: %d\n", head->data);

    return 0;
}
