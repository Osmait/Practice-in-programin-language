#include "stdio.h"
#include <stdlib.h>

typedef struct Nodo {

  int valor;
  struct Nodo *izdo;
  struct Nodo *dcho;

} Nodo;

typedef Nodo Arbol;
Nodo *CrearNodo(int valor) {
  Nodo *nuevoNodo = (Nodo *)malloc(sizeof(Nodo));
  nuevoNodo->valor = valor;
  nuevoNodo->izdo = nuevoNodo->dcho = NULL;
  return nuevoNodo;
}

void DestruirNodo(Nodo *nodo) {
  nodo->izdo = nodo->dcho = NULL;
  free(nodo);
}

void Insertar(Nodo **arbol, int valor) {
  if (*arbol == NULL) {
    *arbol = CrearNodo(valor);

  } else {
    int valorRaiz = (*arbol)->valor;
    if (valor < valorRaiz) {
      Insertar(&(*arbol)->izdo, valor);
    } else {
      Insertar(&(*arbol)->dcho, valor);
    }
  }
}
int Existe(Nodo *arbol, int valor) {
  if (arbol == NULL) {
    return 0;
  } else if (arbol->valor == valor) {
    return 1;
  } else if (valor < arbol->valor) {
    return Existe(arbol->izdo, valor);
  } else {
    return Existe(arbol->dcho, valor);
  }
}

void DeterminarExistencia(Nodo *arbol, int valor) {
  if (Existe(arbol, valor)) {
    printf("El nodo %d existe en el arbol\n", valor);

  } else {
    printf("El nodo %d NO existe en el arbol\n ", valor);
  }
}
int main(void) {
  Nodo *arbol = NULL;
  Insertar(&arbol, 5);
  Insertar(&arbol, 10);
  Insertar(&arbol, 4);
  Insertar(&arbol, 9);
  Insertar(&arbol, 15);
  DeterminarExistencia(arbol, 10);
  DeterminarExistencia(arbol, 3);
  DeterminarExistencia(arbol, 9);
  return 0;
}
