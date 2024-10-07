'''
Cal buscar la informació que es demana de la següent list:

areas_pis = [“Menjador”, 10.15, “Rebedor”, 9.56, “Habitació1”,
              12.34, “Terrassa”, 15.55, “Lavabo”, 7.98, “Cuina”, 
              12, “Habitació2”, 12.23]
(Cal utilitzar els “:” per a que siguin vàlids els prints següents)

Imprimir el segon element
Imprimir l’últim element
Imprimir l’àrea de la terrassa
Imprimir del primer element al tercer element
Imprimir del tercer element a l’últim
Imprimir el total de l'àrea de les dues habitacions
Modificar l’àrea del lavabo i imprimir la nova list area
Afegir l'àrea de “pati interior” i 2.78 a les últimes posicions. Imprimir la nova list area.
Imprimir el total de l’àrea del pis.
'''

#List
areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1",
              12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 
              12, "Habitació2", 12.23]

segon_element = areas_pis[1]
print("Segon element: ", segon_element)

ultim_element = areas_pis[-1]
print("Ultin element: ", ultim_element)

area_terrassa = areas_pis[areas_pis.index("Terrassa") + 1]
print("Area terrassa: ", area_terrassa)

primer_al_tercer = areas_pis[:3]
print("Del primer al tercer element: ", primer_al_tercer)

tercer_al_ultim = areas_pis[:2]
print("Del tercer al ultim: ", tercer_al_ultim)

area_habitacions = areas_pis[areas_pis.index("Habitacio1") + 1] + areas_pis[areas_pis.index("Habitacio2") + 1]
print("Total de l'area de les dos habitacions: ", area_habitacions)

areas_pis[areas_pis.index("Lavabo") + 1] = 8.5
print("Llista l'area del bany modificada: ", areas_pis)


print("Total de l'area pis: ", )




