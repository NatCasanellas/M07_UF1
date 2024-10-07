'''
Demanar a l’usuari que introdueixi 10 números separats per un espai. 
Al acabar, el programa els introduirà en una tupla i els ordenarà 
(major o menor, com volgueu), mostrant per pantalla el contingut 
de la tupla.
'''

#demanar usuari introdueixi 10 numeros seperats per un espai.
entrada = input("Introdueix 10 numeros separats per un espai: ")

#converteix la cadena d'entrada en una llista de numeros
numeros = list(map(int, entrada.split()))

#creacio tupla amb els numeros
tupla_numeros = tuple(numeros)

#ordenar la tupla ascendent
tupla_ordenada = tuple(sorted(tupla_numeros))

#mostrar tupla ordenada
print(f"La tupla ordenada es {tupla_ordenada}")