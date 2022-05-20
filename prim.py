# -*- coding: utf-8 -*-
"""
Created on Fri May 20 11:15:35 2022

@author: david
"""

from funciones import *

def prim(G,N,A):
    
    padre=[]
    #todos son candidatos para ser metidos en AR
    cand = inicializarATrue([], N)
    #distancia de cada nodo al mas cercano en AR
    dist = inicializarAInfinito([], N)
    #solucion
    sol = []
    #escogemos un nodo al azar y lo marcamos como el mas cercano
    D[0]=1
    #indicamos que es el nodo inicial
    padre[0]=-1
    
    cont = 0
    while cont != len(N):
        u = buscarMaximo(cand, D)