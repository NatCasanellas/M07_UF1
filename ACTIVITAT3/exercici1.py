'''
Demanar a l’usuari un nùmero entre 1 i 100. 
Posar els números a una tupla desde 1 fins al número indicat 
per l’usuari. Exemple: usuari indica 34, es crea una tupla i 
es mostra per pantalla els números de l’1 al 34 (imprimint la tupla).
'''

#demanar a l'usuari un numero entre 1 i 100

numero = int(input("Introdueix un numero entre 1 i 100: "))

if 10 <= numero <= 100:
    #creem la tupla amb els numeros de fins el numero usuari
    tupla_numeros = tuple(range(1,numero + 1)) 
    #mostra els numeros del 1 al indicat l'usuari en una tupla
    print(f"Els numeros del 1 al {numero} son: {tupla_numeros}")