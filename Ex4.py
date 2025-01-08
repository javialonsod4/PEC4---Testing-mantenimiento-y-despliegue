import re
import pandas as pd
from faker import Faker
from utils import name_surname, minutes_002040, clean_club

if __name__ == '__main__':

    # Recreamos el dataframe que hemos ido amoldando.
    # Primer ejercicio.
    df = pd.read_csv('data/dataset.csv', sep=';')
    
    # Segundo ejercicio.
    df = name_surname(df)
    for i in range(len(df)):
        if df.loc[i, 'time'] == '00:00:00':
            df.drop(i, inplace=True)

    # Tercer ejercicio.
    t_grouped = list()
    for i in df['time']:
        t = minutes_002040(i)
        t_grouped.append(t)
    df['time_grouped'] = t_grouped

    # CUARTO EJERCICIO.
    # La función 'clean_club' devuelve el nombre del club limpio,
    # por lo que añadiremos a una lista los nombres de los clubes
    # limpios y con la lista añadiremos la nueva columna 'club_clean'.
    c_clean = list()

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