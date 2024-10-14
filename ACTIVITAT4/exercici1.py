'''
(A)Trucar a l’exercici 1 i mostrar per pantalla:
La matriu com la de la imatge de l’exercici 1
La dimensió de la matriu
El tamany de la matriu
Número total d’elements
Tipus d’elements interns

Cada punt ha de vindre acompanyat d’un text on quedi clar 
què s’està mostrant per pantalla
----------------------------------------------------------------
Crearà un ndarray com la de la imatge. La matriu que es mostra 
és una matriu on només es vol números ascendents en la diagonal 
de 0 a 49.  (mirar el següent enllaç)

Guardar la ndarray en un arxiu de nom exercici1.npy.

'''
import numpy as np

def crear_ndarray():
    #crea una matriu de zeros de 50x50
    matriu = np.zeros((50, 50), dtype = int)

    #asigna numeros ascendents a la diagonal
    for i in range(50):
        matriu[i][i] = i

    #guarda la matriu a un archiu .npy
    np.save('exercici1.npy', matriu) 

if __name__=="__main__":
    crear_ndarray()       




