'''
Amb el paquet PANDAS i MATPLOTLIB crear 4 funcions que:
		(Caldrà agafar 10 ciutats)
1 funció que mostri per pantalla, el total de població per ciutat.
1 funció que mostri per pantalla, la densitat per KM2 per ciutat.
1 funció que mostri per pantalla, la densitat per M2 per ciutat.
1 funció main la qual truqui a les 3 funcions i mostri, utilitzant matplotlib, 1 gràfica circular per cada funció mostrant els resultats. (Cal que la gràfica tingui llegenda i cal mostrar el % en cada “quesito”). Si veieu que en aquest format, la llegenda es sobreposa, agafeu una mostra des del main.
'''

import pandas as pd
import matplotlib.pyplot as plt

arxiu_list = './ACTIVITAT5/List of world cities by population density.csv'
list_w = pd.read_csv(arxiu_list) #data frame

#Selecciona una mostra de 10 ciutats
ciutats_sample = list_w.sample(10)

#Funció 1: mostrar el total de població per ciutat
def mostrar_poblacio(ciutats_sample):
    poblacio_per_ciutat = ciutats_sample[['City', 'Population']]
    print(poblacio_per_ciutat)
    return poblacio_per_ciutat

#Funcio 2: mostra la densitat per Km2 per ciutat
def mostrar_densitat_km2(ciutats_sample):
    densitat_km2 = ciutats_sample[['City', 'Density (/km²']]
    print(densitat_km2)
    return densitat_km2

#Funcio 3: mostrar la densitat per m2 per ciutat
def mostrar_densitat_m2(ciutats_sample):
    #
    ciutats_sample['Density (/mi²)'] = ciutats_sample['Population'] / (ciutats_sample['Area (km²)'] * 1_000_000)
    return ciutats_sample[['City', 'Density (/mi²)']]

#Funcio main: mostra dades grafiques
def main():
    #dades de cada funcio
    poblacio_data = mostrar_poblacio(ciutats_sample)
    densitat_km2_data = mostrar_densitat_km2(ciutats_sample)
    densitat_m2_data = mostrar_densitat_m2(ciutats_sample)
    
	#creem grafica circucular
    plt.figure(figsize = (12, 12))
    
	#grafica per poblacio
    plt.subplot(3, 1, 1)
    plt.pie(poblacio_data['Population'], labels = poblacio_data['City'], autopct = '%1.1f%%')
    plt.title('Distribucio de la Poblacio per Ciutat')
    plt.legend(loc = 'upper right', bbox_to_anchor = (1.3, 1))

	#grafica densitat per km2
    plt.subplot(3, 1, 2)
    plt.pie(densitat_km2_data['Density (per km2)'], labels = densitat_km2_data['City'], autopct = '%1.1f%%')
    plt.title('Distribucio de la Densitat per km² per Ciutat')
    plt.legend(loc = 'upper right', bbox_to_anchor = (1.3, 1))

    
	#grafica densitat per m2
    plt.subplot(3, 1, 3)
    plt.pie(densitat_m2_data['Density (per m2)'], labels = densitat_m2_data['City'], autopct = '%1.1f%%')
    plt.title('Distribució de la Densitat per m² per Ciutat')
    plt.legend(loc = 'upper right', bbox_to_anchor = (1.3, 1))

	#ajustar el layout
    plt.tight_layout()
    plt.show()
    

#executar la funcio principal
main()	