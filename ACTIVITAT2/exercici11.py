#Exercici que mostra la taula de multiplicar

#Demana un numero a l'usuari
numero = int(input("Introdueix un numero: "))

#Mostra la taula de multiplicar del numero indicat
print(f"Taula de multiplicar del {numero}: ")
for i in range(1,11):
    resultat = numero * i
    print(f"{numero} x {i} = {resultat}")
