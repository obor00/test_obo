#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ITERATIONS 10000
#define SIZE 1024 // Change the size as needed

int main() {
    clock_t start, end;
    double cpu_time_used;

    start = clock();

    for (int i = 0; i < ITERATIONS; i++) {
        void *ptr = malloc(SIZE);
        if (ptr == NULL) {
            fprintf(stderr, "Memory allocation failed at iteration %d\n", i);
            return 1;
        }
        free(ptr);
    }

    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;

    printf("Time taken for %d iterations of malloc/free: %f seconds\n", ITERATIONS, cpu_time_used);

    return 0;
}
