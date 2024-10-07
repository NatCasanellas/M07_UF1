'''
Llistat de notes. Crear una lista amb 6 assignatures 
(poden ser mòduls de cicles o assignatures de secundaria). 
Demana a l’usuari que indiqui les notes de cada assignatura 
i emmagatzema-les en una altra llista. Mostrar per pantalla 
el missatge A <assignatura> ha tret <nota>. 
Intenta millorar aquest programa utilitzant altres 
tipus de dades explicats. Cal que l’exercici tingui les dues versions.
'''
#Llistat moduls
moduls = ["Programacio", "Bases de dades", "Llenguatge de marques", "Disseny", "Entorn client", "Entorn servidor"]

#Llista per emmagatzemar notes
notes = []

#
for modul in moduls:
    nota = float(input(f"Introdueix la nota del {modul}: "))
    notes.append(nota)

for i in range(len(moduls)):
    print(f"A {moduls[i]} ha tret {notes[i]} ")    

###########################################################################
#diccionari moduls
moduls_notes = {}

moduls = ["Programacio", "Bases de dades", "Llenguatge de marques", "Disseny", "Entorn client", "Entorn servidor"]

for modul in  moduls:
    nota = float(input(f"Introdueix la nota del {modul}: "))
    moduls_notes[modul] = nota

for modul, nota in moduls_notes.items():
    print(f"A {modul} ha tret {nota}")    
