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
def inicializarAMenosInfinito(lista, N):
    for i in range(N):
        lista.append(float('-inf'))
    return lista


#dado un grafo (G) inserta en una lista todos sus nodos
def anadirNodos(G):
    N=[]
    for i in range(len(G)):
        N.append(i)
    return N


#dada un grafo (G) inserta en una lista todas sus aristas
def anadirAristas(G):
    A=[]
    for i in range(len(G)):
        for j in range(i, len(G)):
            if G[i][j]>0:
                A.append((i,j))
                
    return A
               
    
#dada una lista de nodos y una lista de distancias D, devuelve el nodo con mayor D de entre aquellos cuyo cand es true
def buscarMaximo(cand,D):
    aux= float('-inf')
    sol=0
    for i in range(len(D)):
        if cand[i]==True and D[i]>aux:
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


#dada la direccion de un fichero con la informacion del grafo, guarda dicha informacion en las variables G (matriz 2x2), N (valor) y A (valor)
def almacenarNodo(direccion):
    f = open(direccion, 'r')
    N = int(f.readline())
    A = int(f.readline())
    G=[]
    
    for i in range(N):
        G.append([])
        for j in range(N):
            G[i].append(0)
    linea = f.readline()
    
    while linea != "":
        vLinea = linea.split(" ")        
        i= int(vLinea[0])
        j= int(vLinea[1])
        G[i][j]= float(vLinea[2])
        G[j][i]= float(vLinea[2])
        linea = f.readline()
    return (G,N,A)