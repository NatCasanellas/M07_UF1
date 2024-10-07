'''
Crear una tupla amb els mesos de l’any. Demanar a l’usuari 
que posi un número entre 0 i 12 i mostrar per pantalla el 
mes corresponent al número indicat per l’usuari. 
El programa finalitza només quan l’usuari posa 0.
'''
#tupla mesos de l'any
tupla_mesos = ("Gener", "Febrer", "Març", "Abril", "Maig", "Juny", "Juliol",
              "Agost", "Setembre", "Octubre", "Novembre", "Desembre"
              )

while True: #bucle while
    #demanar usuari posi numero netre 0 i 12
    numero = int(input("Introdueix un numero entre 0 i 12(0 per sortir): "))

    if 1 <= numero <= 12:
        print(f"El mes es: {tupla_mesos[numero - 1]}")
    #el progrmama finalitza perque ha introduit 0
    elif numero == 0:
        print("Adeu!")
        break #surt del bucle