'''
Trucar a l’exercici 2 i mostrar per pantalla:
1.Les matrius com les de la imatge d l’exercici 2.
2.Número total d’elements
3.La dimensió de la matriu
4.Tipus d’elements interns
5.El tamany de la matriu


Una funció per crear una array com la de la imatge:
[88, 23, 39, 41]

Una funció per crear una array com la de la imatge:
[[76.4, 21.7, 38.4], [41.2, 52.8, 68.9]]

Una funció per crear una array com la de la imatge:
12
4
9
8
'''
import numpy as np

#array unidimensional
def array_unidimensional():
    arr = np.array([88, 23, 39, 41])
    print("Array 1:")
    print(arr)
    print("Numero total d'elements: ", arr.size)
    print("Dimensio de la matriu: ", arr.shape)
    print("Tipus d'elements interns: ", arr.dtype)
    print("Mida en bytes de la matriu: ", arr.nbytes)


#array bidimensional
def array_bidimensional():
    arr = np.array([[76.4, 21.7, 38.4], [41.2, 52.8, 68.9]])
    print("Array bidimensional: ")
    print(arr)
    print("Numero total d'elements: ", arr.size)
    print("Dimensio de la matriu: ", arr.shape)
    print("Tipus d'elements interns: ", arr.dtype)
    print("Mida en bytes de la matriu: ", arr.nbytes)

#array numeros
def array_numeros():
    arr = np.array([12, 4, 9, 8])
    print("Array numeros: ")
    print(arr)
    print("Numero total d'elements: ", arr.size)
    print("Dimensio de la matriu: ", arr.shape)
    print("Tipus d'elements interns: ", arr.dtype)
    print("Mida en bytes de la matriu: ", arr.nbytes)    

#trucada arrays
array_unidimensional()
array_bidimensional()
array_numeros()

