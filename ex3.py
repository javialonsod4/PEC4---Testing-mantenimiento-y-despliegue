import os
import pandas as pd
import matplotlib.pyplot as plt
from utils import name_surname, minutes_002040

if __name__ == '__main__':

    # Recreamos el dataframe que hemos ido amoldando.
    # Primer ejercicio.
    df = pd.read_csv('data/dataset.csv', sep=';')

    # Segundo ejercicio.
    df = name_surname(df)
    for i in range(len(df)):
        if df.loc[i, 'time'] == '00:00:00':
            df.drop(i, inplace=True)

    # TERCER EJERCICIO.
    # Ejecutamos la función 'minutes_002040' a cada uno de los valores
    # de la columna 'time', lo añadimos a una lista y creamos la nueva
    # columna 'time_grouped'.
    t_grouped = []

    for i in df['time']:
        t = minutes_002040(i)
        t_grouped.append(t)

    df['time_grouped'] = t_grouped

    # Mostramos los 15 primeros valores del nuevo dataframe.
    print('\nLos nuevos 15 valores son:')
    print(df.head(15))

    # Creamos un nuevo dataframe con el número de ciclistas para cada
    # franja de tiempo que hemos definido.
    df_grouped = df.groupby('time_grouped', as_index=False)[['dorsal']].count()
    df_grouped.columns = ['time_grouped', 'num_bikers']

    # Mostramos los resultados.
    print('\nEste es el nuevo dataframe:')
    print(df_grouped)

    # Para poder guardar el histograma, debemos crear el nuevo directorio.
    NEW_FOLDER = 'img'
    try:
        os.mkdir(NEW_FOLDER)
    except FileExistsError:
        print(f'\nFolder "{NEW_FOLDER}" already exists.')

    # Ahora generamos el histograma y lo guardamos en el nuevo directorio.
    plt.figure()
    plt.bar(df_grouped['time_grouped'], df_grouped['num_bikers'], width=1)
    plt.xticks(rotation=45)
    plt.title('Number of bikers for each time range group')
    plt.xlabel('Time range group')
    plt.ylabel('Number of bikers')

    plt.savefig('img/histograma.png')
    plt.show()
