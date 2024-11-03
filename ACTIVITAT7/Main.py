from create import create_contact
from read import read_contacts
from update import update_contact
from delete import delete_contact
from create_table import create_table

def manu():
    print("1. Crear contacte")
    print("2. Llegir contactes")
    print("3. Actualitzar contacte")
    print("4. Eliminar contacte")
    print("0. Sortir")

    option = int(input("Selecciona una opcio: "))
    return option

if __name__ == "__main__": 
    create_table() 
    while True: 
        option = menu() 
        if option == 1: 
            nom = input("Nom: ") 
            cognom = input("Cognom: ") 
            email = input("Email: ") 
            telefon = input("Telefon: ") 
            direccio = input("Direccio: ") 
            create_contact(nom, cognom, email, telefon, direccio) 
        elif option == 2: 
            read_contacts() 
        elif option == 3: 
            id = int(input("ID del contacte a actualitzar: ")) 
            nom = input("Nou nom: ") 
            apellido = input("Nou cognom: ") 
            email = input("Nou email: ") 
            telefono = input("Nou telefon: ") 
            direccion = input("Nova direccio: ") 
            update_contact(id, nom or None, cognom or None, email or None, telefon or None, direccio or None) 
        elif option == 4: 
            id = int(input("ID del contacto a eliminar: ")) 
            delete_contact(id) 
        elif option == 0: 
            break 
        else: print("Opcio no valida. Intenta-ho de nou.")  