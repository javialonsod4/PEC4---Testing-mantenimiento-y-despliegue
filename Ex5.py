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
    
    # Cuarto ejercicio.
    c_clean = list()
    for c in df['club']:
        c_clean.append(clean_club(c))
    df['club_clean'] = c_clean
    
    # QUINTO EJERCICIO.
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
    print('\nEl primer ciclista de la UCSC quedó en posición {} de {}'
          ' ciclistas.'.format(pos_first_ucsc, total_bikers))

    # Mostramos el porcentaje del ciclista.
    per_first_ucsc = (pos_first_ucsc / total_bikers) * 100
    print('\nEsto representa un {0:.2f} porciento.'.format(per_first_ucsc))