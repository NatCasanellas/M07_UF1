'''
Crear un diccionari de divises amb els seus símbols 
(exemple: Euro:€…). Demana a l’usuari una divisa i 
mostra el seu símbol. Si la divisa no està al diccionari 
mostra un missatge.
'''

#diccionari divises amb els seus simbols
divises = {
    "Euro": "€",
    "Dolar": "$",
    "Lliura": "£",
    "Ien": "¥",
    "Franc suis": "CHF",
    "Dolar australia": "A$"
}

#demana al usuari que introdueixi una divisa
divisa = input("Introdueix el nom de la divisa: ")

if divisa in divises:
    print(f"El simbol de {divisa} es {divises[divisa]}")
else:
    print(f"La divisa {divisa} no es troba al diccionari")    