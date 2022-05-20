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