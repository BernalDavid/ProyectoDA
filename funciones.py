# -*- coding: utf-8 -*-
"""
Created on Fri May 20 11:01:26 2022

@author: david
"""

#En este fichero se guardan las funciones auxiliares que se necesiten

#dada una lista vacia y su tamano, devuelve la lista inicializada a true
#posible entrada: lista=[], 3
#posible salida: lista= [true, true, true]
def inicializarATrue(lista,N):
    for i in range(N):
        lista.append(True)
    return lista


#dada una lista vacia y su tamano, devuelve la lista inicializada a infinito
#posible entrada: lista=[], 3
#posible salida: lista= [inf, inf, inf]
def inicializarAInfinito(lista, N):
    for i in range(N):
        lista.append(float('inf'))
    return lista

#dada una lista de nodos y una lista de distancias D, devuelve el nodo con mayor D de entre aquellos cuyo cand es true
def buscarMaximo(cand,D):
    aux= 100
    sol=0
    for i in range(len(D)):
        if cand[i]==True and D[i]<aux:
            aux=D[i]
            sol=i
    return sol


#dado un grafo (G) y un nodo (n), devuelve una lista de nodos adyacentes a n
def adyacentes(G, n):
    lista=[]
    for i in range(len(G)):
        if G[n][i]>0:
            lista.append(i)
    return lista