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

arxiu_test = './ACTIVITAT5/test.csv'
test = pd.read_csv(arxiu_test) #data frame


#llista ID's
ids = [3, 13, 34, 56, 70, 85, 110, 120, 210, 400]


#Funcio 1: mostra el clock speed segons l'ID del mobil
def mostrar_clock_speed(train, ids):
        return test[test['id'].isin(ids)][['id', 'clock_speed']]


#Funcio 2: mostra el megapixels segons l'ID del mobil
def mostrar_megapixels(test, ids):
        return test[test['id'].isin(ids)][['id', 'megapixels']]


#Funcio 3: mostra la baterry power segons l'ID del mobil
def mostrar_battery_power(test, ids):
        return test[test['id'].isin(ids)][['id', 'battery_power']]


#Funcio main: el main truca a les 3 funcions i les mostra utilitzant matplotlib
def main(test, ids):
        #dades de cada funcio
        clock_speed_data = mostrar_clock_speed(test, ids)
        megapixels_data = mostrar_megapixels(test, ids)
        battery_power_data = mostrar_battery_power(test, ids)

        #configuracio de la grafica
        fig, axs = plt.subplots(3, 1, figsize=(10, 15))

        #grafica de barres clock speed
        axs[0].bar(clock_speed_data['id'], clock_speed_data['clock_speed'], color = 'blue')
        axs[0].set_title("Clock Speed ID")
        axs[0].set_xlabel("ID")
        axs[0].set_ylabel("Clock Speed")
        axs[0].legend(["Clock Speed"])

        #grafica barres megapixels
        axs[1].bar(megapixels_data['id'], megapixels_data['mepgapixels'], color = 'red')
        axs[1].set_title("Megapixels ID")
        axs[1].set_xlabel("ID")
        axs[1].set_ylabel("Megapixels")
        axs[1].legend(["Megapixels"])

        #grafica barres battery power
        axs[2].bar(battery_power_data['id'], battery_power_data['battey_power'], color = 'yellow')
        axs[2].set_title("Battery Power ID")
        axs[2].set_xlabel("ID")
        axs[2].set_ylabel("Battery Power")
        axs[2].legend(["Battery Power"])

        #mostra la grafica
        plt.tight_layout()
        plt.show()

        #executar funcio main
        main(test, ids)
