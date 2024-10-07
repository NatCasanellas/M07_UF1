#Demanar a l’usuari que introdueixi 2 valors 
# i mostrar, per pantalla, quin és el més gran. 
# (Utilitzar operador correcte)

#Demanar 2 valors a l'usuari
valor1 = int(input("Introdueix el primer valor: "))
valor2 = int(input("Introdueix el segon valor: "))

#Compara els dos valors i mostra el mes gran, utilitzant el if i l'perador >
if valor1 > valor2:
    print(f"El valor mes gran es: {valor1}")
elif valor2 > valor1:
    print(f"El valor mes gran es: {valor2}")
else:
    print("Els dos valors son iguals")        
