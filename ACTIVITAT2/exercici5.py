#Demanar a l’usuari un número. Indicar si el número 
# inserit per l’usuari és parell o senar.

#demanar un numero a l'usuari
numero = int(input("Introdueix un numero: "))

#comprovar si es un parell o senar
if numero % 2 == 0:
    print(f"El numero {numero} es parell")
else:
    print(f"El numero {numero} es senar")    