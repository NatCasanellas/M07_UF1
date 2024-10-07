#Exercici 2

#Demanar a l’usuari que introdueixi un valor en €, 
# seguidament demanar que introdueixi el IVA a 
# aplicar-hi (4%, 10% o 21%) i finalment mostrar, 
# per pantalla, el resultat del valor indicat 
# per l’usuari, el % d’IVA demanat per l’usuari 
# i el valor final amb l’IVA afegit. Si no afageix 
# el IVA correcte, tornar a demanar el IVA fins que 
# posi un dels 3 vàlids.

#funcio per calcular l'iva
def calcular_iva(valor, iva_percentatge):
    iva = valor * iva_percentatge / 100
    return valor + iva

#Demana el valor a l'usuari
valor = float(input("Introdueix un valor en €: "))

#demana el % de l'iva 
iva_parcentatge = None
while iva_parcentatge not in [4, 10, 21]:
    iva_parcentatge = int(input("Introdueix el % d'iva (4%, 10%, 21%):"))

#Calcul del valor amb l'iva afegit
valor_final = calcular_iva(valor, iva_parcentatge)

#Resultat
print(f"Valor original: {valor}€")
print(f"IVA aplicat: {iva_parcentatge}%")
print(f"Valor final amb IVA: {valor_final}€")