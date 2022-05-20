# -*- coding: utf-8 -*-
"""
Created on Fri May 20 11:15:35 2022

@author: david
"""

from funciones import *

def prim(G,N,A):
    
    padre=[0,0,0,0,0,0,0]
    #todos son candidatos para ser metidos en AR
    cand = inicializarATrue([],len(N))
    #distancia de cada nodo al mas cercano en AR
    D = inicializarAMenosInfinito([], len(N))
    #solucion
    sol = anadirAristas(G)
    #escogemos un nodo al azar y lo marcamos como el mas cercano
    D[0]=-1
    #indicamos que es el nodo inicial
    padre[0]=-1
    
    cont = 0
    while cont != len(N):
        #devuelve el nodo con mayor D entre aquellos cuyo Cand es true
        u = buscarMaximo(cand, D)
        #el nodo u pasa a estar en AR
        cand[u]=False
        
        if padre[u]!=-1:
            if (padre[u],u) in sol:
                sol.remove((padre[u],u))
            else:
                sol.remove((u,padre[u]))
            
        for v in adyacentes(G, u):
            if cand[v]==True and G[u][v] > D[v]:
                D[v]=G[u][v]
                padre[v]=u
        cont=cont+1
    return sol


g4 = [[ 0, 28,  0,  0,  0, 10,  0],
      [28,  0, 16,  0,  0,  0, 40],
      [ 0, 16,  0, 12,  0,  0,  0],
      [ 0,  0, 12,  0, 22,  0, 18],
      [ 0,  0,  0, 22,  0, 25, 24],
      [10,  0,  0,  0, 25,  0,  0],
      [ 0, 40,  0, 18, 24,  0,  0]]

N=anadirNodos(g4)
A=anadirAristas(g4)
S=prim(g4,N,A)
print(S) 