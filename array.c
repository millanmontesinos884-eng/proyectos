#include <stdio.h>
#include <stdlib.h>


int main(){
    int n_elementos;
    printf("Introduce el numero de elementos que tendrá el array:\n");
    scanf("%d", &n_elementos);
    int array[n_elementos];
    for (int i = 0; i <n_elementos; i++){
        printf("introduce el elemento %d\n", i);
        scanf("%d", &array[i]);//Introducir el valor y se guardará en la posición actual del array-.
        

    } //final bucle for
    for (int i = 0; i < n_elementos; i++){
        printf("El elemento %d introducido es %d: \n", i + 1, array[i]);
    }// final del segundo bucle for

    for (int i= 0; i <n_elementos; i++){
        for(int j = 0; j < array[i]; j =array[i]-1 )
    }//final bucle i
    return 0;
}