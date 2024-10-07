#Demanar a l’usuari dos valors. 
# Una vegada s’executa el programa, aquest ha de 
# mostrar el resultat (suma, resta, divisió o multiplicació)  
# per pantalla.

#Demana els dos valors a l'usuari
valor1 = int(input("Introdueix el primer valor: "))
valor2 =  int(input("Introdueix el segon valor: "))

#operacio a realitzar
operacio = input("Quina operacio vols fer?(suma, resta, divisio, multiplicacio): ").lower()

#Realitzar l'operacio segons l'entrada de l'usuari
if operacio == "suma":
    resultat = valor1 + valor2
    print(f"El resultat de la suma es: {resultat}")
elif operacio == "resta":
    resultat = valor1 - valor2
    print(f"El resultat de la resta es: {resultat}")
elif operacio == "divisio":
    if valor2 != 0:
        resultat = valor1 -valor2
        print(f"El resultat de la divisio es: {resultat}")
    else:
        print("No es pot dividir per zero")
elif operacio =="multiplicacio":
    resultat = valor1 * valor2
    print(f"El resultat de la multiplicacio es: {resultat}")
else:
    print("No es correcte")                   