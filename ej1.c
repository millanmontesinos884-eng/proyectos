#include <stdio.h>
#include <stdlib.h>

void sstf(int pista_solicitada[], int n_elementos, int pos_inicial){
     int distancia_total = 0;
while (n_elementos > 0){
    int distancia_tramo = 0;
    int valor_actual = 0;
    int pista_ganadora = 0;
    int indice_ganador = 0;
    int pista_cerca = 200;
    for (int i = 0; i < n_elementos; i++){
        valor_actual = abs(pista_solicitada[i] - pos_inicial);
        
        if (valor_actual < pista_cerca){
            pista_cerca = valor_actual;
            pista_ganadora = pista_solicitada[i];
            indice_ganador = i;
        }

    }
    distancia_tramo = pista_cerca;
    distancia_total = distancia_total +  distancia_tramo;
    printf("Pista visitada: %d\n", pista_ganadora);
    pos_inicial = pista_ganadora;
    for(int j =indice_ganador; j <n_elementos - 1; j++){
     pista_solicitada[j] = pista_solicitada[j+1];   
}
    n_elementos --;
    }
printf("Distancia total recorrida:%d\n", distancia_total);

}

int main(){
//pedir numero de solicitudes
int n_elementos;
int pista_solicitada[20];
int pos_inicial;
//Introduce el numero de solicitudes de disco
printf("Introduce el numero de elementos:\n");
scanf("%d", &n_elementos);

// Introduce las pistas
printf("Introduce el numero de pistas una por una :\n");
for(int i = 0; i < n_elementos; i++){
printf("pista_solicitada %d: ", i + 1);
scanf("%d", &pista_solicitada[i]);
}
//Introduce la posicion inicial
printf("Introduce la posicion inicial:\n");
scanf("%d", &pos_inicial);

//Mostrar resumen de los datos introducidos//
    printf("\n--- DATOS INTRODUCIDOS ---\n");
    printf("pista_solicitada:");
    for (int i = 0; i < n_elementos ; i++)

    printf("%d ", pista_solicitada[i]);
    printf("\nCabezal inicial: %d\n", pos_inicial);

    // Ejecutar las simulaciones con tus datos dinámicos
   sstf (pista_solicitada, n_elementos, pos_inicial);


    return 0;


}