'''This module solves all the exercises in its order.'''

import os
import pandas as pd
import matplotlib.pyplot as plt
from utils import name_surname, minutes_002040, clean_club

if __name__ == "__main__":

    # PRIMER EJERCICIO:
    # Importación del dataset y EDA
    print('PRIMER EJERCICIO.')

    # Importamos el dataset.
    df = pd.read_csv('data/dataset.csv', sep=';')

    # Mostramos los 5 primeros valores.
    print('\nLos 5 primeros valores son:')
    print(df.head())

    # Mostramos el número de ciclistas que participaron en
    # función de los dorsales, pues los nombres pueden estar
    # repetidos.
    num_bikers = len(df['dorsal'].unique())
    print('\nEl número de ciclistas es:', num_bikers)

    # Columnas del dataframe.
    cols = list(df.columns)
    print(f'\nLas columnas del dataframe son:\n{cols}')

    # SEGUNDO EJERCICIO:
    # Anonimizar los ciclistas. Limpiar el dataset.
    print('\n\nSEGUNDO EJERCICIO.')

    # Ejecutamos la función 'name_surname'.
    df = name_surname(df)

    # Y mostramos los 5 primeros valores.
    print('\nLos nuevos 5 primeros valores son:')
    print(df.head())

    # Eliminamos los ciclistas con tiempo '00:00:00'.
    for i in range(len(df)):
        if df.loc[i, 'time'] == '00:00:00':
            df.drop(i, inplace=True)

    # Mostramos los ciclistas que quedan.
    num_bikers_with_time = df['dorsal'].count()
    print(f'\nQuedan {num_bikers_with_time} ciclistas.')

    # Mostramos los 5 primeros valores del nuevo dataframe.
    print('\nLos nuevos 5 primeros valores son:')
    print(df.head())

    # Mostramos el ciclista con el dorsal 1000.
    print('\nEl ciclista con el dorsal 1000 es:')
    print(df[df['dorsal'] == 1000])

    # TERCER EJERCICIO:
    # Agrupamiento de los minutos. Histograma.
    print('\n\nTERCER EJERCICIO.')

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

    # CUARTO EJERCICIO:
    # Clubs ciclistas.
    print('\n\nCUARTO EJERCICIO.')

    # La función 'clean_club' devuelve el nombre del club limpio,
    # por lo que añadiremos a una lista los nombres de los clubes
    # limpios y con la lista añadiremos la nueva columna 'club_clean'.
    c_clean = []

    for c in df['club']:
        c_clean.append(clean_club(c))

    df['club_clean'] = c_clean

    # Mostramos los nuevos valores.
    print('\nLos nuevos 15 primeros valores son:')
    print(df.head(15))

    # Creamos un nuevo dataframe con la cuenta de ciclistas poor cada
    # club, y lo ordenamos en orden descendente por el número de ciclistas.
    df_club = df.groupby('club_clean', as_index=False)[['dorsal']].count()
    df_club.columns = ['club', 'num_bikers']
    df_club.sort_values(by='num_bikers', ascending=False, inplace=True)

    # Mostramos los primeros resultados a modo de comprobación.
    print('\nLos 5 primeros valores del nuevo dataframe son:')
    print(df_club.head())

    # QUINTO EJERCICIO.
    # Unió Ciclista Sant Cugat (UCSC).
    print('\n\nQUINTO EJERCICIO.')

    # Mostramos los ciclistas de la UCSC.
    print('\nLos ciclistas de la UCSC son:')
    print(df[df['club_clean'] == 'UCSC'])

    # Como el dataframe está ordenado ascendentemente por los tiempos,
    # seleccionamos el nombre del primer ciclista de los que pertenecen
    # a la UCSC.
    first_ucsc = df[df['club_clean'] == 'UCSC'].iloc[0, 1]
    print('\nEl nombre del primer ciclista de la UCSC es:', first_ucsc)

    # Recorremos la columna 'club_clean' hasta que encontramos un ciclista
    # de la UCSC.
    for i in range(len(df['club_clean'])):
        if df.iloc[i, 5] == 'UCSC':
            break

    # El bucle comienza en el valor 0, por tanto, debemos seleccionar el
    # siguiente valor para conocer la posición real del ciclista.
    pos_first_ucsc = i + 1
    total_bikers = len(df['club_clean'])
    print(f'\nEl primer ciclista de la UCSC quedó en posición {pos_first_ucsc}'
          f' de {total_bikers} ciclistas.')

    # Mostramos el porcentaje del ciclista.
    per_first_ucsc = (pos_first_ucsc / total_bikers) * 100
    print(f'\nEsto representa un {"%.2f"%per_first_ucsc} porciento.')
