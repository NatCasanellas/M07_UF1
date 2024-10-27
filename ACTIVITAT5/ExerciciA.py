'''
Amb el paquet PANDAS i MATPLOTLIB crear 4 funcions que:

1 funció que mostri per pantalla, la quantitat de casos total per mes per país (agafar 10 països) (agafar 4 mesos).
1 funció que mostri per pantalla, les morts totals per mes per país (agafar 10 països) (agafar 4 mesos) del 2021.
1 funció que mostri per pantalla la “reproduction_rate” per mes per país (agafar 10 països) (agafar 4 mesos).
1 funció main la qual truqui a les 3 funcions i mostri, utilitzant matplotlib, 1 gràfica de línies per cada funció mostrant els resultats. (Cal que la gràfica tingui llegenda)
'''

import pandas as pd
import matplotlib.pyplot as plt

arxiu_covid = './ACTIVITAT5/df_covid19_countries.csv'
covid = pd.read_csv(arxiu_covid)

#selecionem 10 paisos i 4 mesos
paisos = covid['location'].unique()[:10]
mesos = ['2021-02', '2021-03', '2021-04', '2021-05']


#convertim la columna 'date' a format datetime per operacions per mes
covid['date'] = pd.to_datetime(covid['date'])
covid['year_month'] = covid['date'].dt.to_period('M')

#funció 1: Casos totals per mes per país
def total_casos_mes():
    data = covid[covid['location'].isin(paisos) & covid['year_month'].isin(paisos)]
    casos_per_mes = data.groupby(['location', 'year_month'])['new_cases'].sum().unstack()
    print("Casos totals per mes per país:")
    print(casos_per_mes)
    return casos_per_mes

#funció 2: Morts totals per mes per país per 2021
def total_morts_mes():
    data = covid[(covid['location'].isin(paisos)) & (covid['year_month'].isin(paisos))]
    morts_per_mes = data.groupby(['location', 'year_month'])['new_deaths'].sum().unstack()
    print("Morts totals per mes per país:")
    print(morts_per_mes)
    return morts_per_mes

#funció 3: Taxa de reproducció per mes per país
def taxa_reproduccio_per_mes():
    data = covid[(covid['location'].isin(paisos)) & (covid['year_month'].isin(paisos))]
    taxa_reproduccio = data.groupby(['location', 'year_month'])['reproduction_rate'].mean().unstack()
    print("Taxa de reproducció per mes per país:")
    print(taxa_reproduccio)
    return taxa_reproduccio

#funció principal per cridar les altres funcions i mostrar els resultats amb gràfics de línies
def main():
    casos_per_mes = total_casos_mes()
    morts_per_mes = total_morts_mes()
    taxa_reproduccio = taxa_reproduccio_per_mes()

    #configuració de gràfics per mostrar els resultats
    fig, axs = plt.subplots(3, 1, figsize=(10, 15))
    
    #grafica de casos totals
    casos_per_mes.T.plot(ax=axs[0], marker='o')
    axs[0].set_title("Casos totals per mes per pais")
    axs[0].set_xlabel("Mes")
    axs[0].set_ylabel("Casos Totals")
    axs[0].legend(title="País")

    #grafica de morts totals
    morts_per_mes.T.plot(ax=axs[1], marker='o', color='tab:red')
    axs[1].set_title("Morts totals per mes per pais")
    axs[1].set_xlabel("Mes")
    axs[1].set_ylabel("Morts Totals")
    axs[1].legend(title="País")

    #grafica de taxa de reproducció
    taxa_reproduccio.T.plot(ax=axs[2], marker='o', color='tab:green')
    axs[2].set_title("Taxa de reproducció per mes per pais")
    axs[2].set_xlabel("Mes")
    axs[2].set_ylabel("Taxa de Reproducció")
    axs[2].legend(title="País")


    #ajustar el layout
    plt.tight_layout()
    plt.show()
    

#executar la funcio principal
main()	