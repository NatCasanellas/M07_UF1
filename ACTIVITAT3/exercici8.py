'''
Demanar a l’usuari que posi 10 números separats per espais. 
Afegir aquests números a una llista. Calcular la suma de tots 
els números i la seva mitjana i afegir aquests 2 números a la llista. 
Mostrar per pantalla la llista.

Exemple mostra per pantalla.
Números de l’usuari:
suma total:
mitjana:
'''
#Demanar usuari posi 10 numeros separats per espais
intr_numeros = input("Introdueix 10 numeros separats per espais: ")

#Afegir els numeros en una llista
numeros = list(map(int, intr_numeros.split()))

#Calcular la suma de tots els numeros i la seva mitjana
suma_total = sum(numeros)
mitjana = suma_total / len(numeros)

#afageix la suma i la mitjana a la llista
numeros.append(suma_total)
numeros.append(mitjana)

#Mostra per pantalla
print("Numeros de l'usuari: ", numeros[:-2])
print("Suma total: ", suma_total)
print("Mitjana: ", mitjana)
