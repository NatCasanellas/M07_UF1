#Demanar a l’usuari que introdueixi un número. 
# Mostrar per pantalla la suma de tots els números 
# començant amb l’1 fins el número indicat per l’usuari.

#Demana un numero a l'usuari
numero = int(input("Introdueix un numero: "))

#inicialitza la suma
suma_total = 0

#bucle
for i in range(1, numero + 1):
    suma_total += i

#resultat
print(f"La suma de tots ls numero de l'1 fins al {numero} es: {suma_total}")    
