'''
Demanar a l’usuari un número de l’1 al 10 i mostrar per pantalla 
la seva taula de multiplicar fins el 10. 
Exemple: l’usuari marca 3, 
es mostra per pantalla: 3,6,9,12,15,18,21,24,27 i 30
'''

#Demanar l'usuari un numero de l'1 fins el 10

numero = int(input("Introdueix un numero de l'1 al 10: "))

if 1 <= numero <= 10:
    #taula de multiplicar del numero indicat per l'usuari
    for i in range(1, 11):
        resultat = numero * i
        if i == 10:
            print(resultat)
        else:
            print(resultat, )    


