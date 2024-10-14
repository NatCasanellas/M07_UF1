'''
Trucar a l’exercici 1 i mostrar per pantalla:
1. La matriu com la de la imatge de l’exercici 1
2. La dimensió de la matriu
3. El tamany de la matriu
4. Número total d’elements
5. Tipus d’elements interns

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
    #crear un ndarray amb numeros ascendents la diagonal de 0 a 49
    arr = np.diag(np.arange(50))

    print("La matriu es: ")
    print(arr)
    
    print("La dimensio de la matriu es: ", arr.shape)
    print("El tamany de la matriu en bytes es: ", arr.nbytes)
    print("El numero total d'elements de la matriu es: ", arr.size)
    print("El tipus d'elements interns es: ",arr.dtype)

    #trucar
    crear_ndarray()