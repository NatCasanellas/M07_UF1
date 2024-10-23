'''
Amb el paquet PANDAS i MATPLOTLIB crear 4 funcions que:
		(Caldrà agafar els següents 10 ID’s com a mostres:  3,13,34,56,70,85,110,120,210,400).
1 funció que mostri per pantalla, el clock speed segons  l’ID del mòbil.
1 funció que mostri per pantalla, els megapixels segons l’ID del mòbil.
1 funciño que mostri per pantalla, la battery power segons l’ID del mòbil.
1 funció main la qual truqui a les 3 funcions i mostri, utilitzant matplotlib, 1 gràfica barres per cada funció mostrant els resultats. (Cal que la gràfica tingui llegenda)
'''

import pandas as pd
import matplotlib.pyplot as plt

arxiu_test = 'test.csv'
arxiu_train = 'train.csv'

df = pd.read_csv(arxiu_test)
print(df)


#Funcio 1: mostra el clock speed segons l'ID del mobil


#Funcio 2: mostra el megapixels segons l'ID del mobil

#Funcio 3: mostra la baterry power segons l'ID del mobil

#Funcio main: el main truca a les 3 funcions i les mostra utilitzant matplotlib