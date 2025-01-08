import pandas as pd
from utils import name_surname

if __name__ == '__main__':

    # Recreamos el dataframe que hemos ido amoldando.
    # Primer ejercicio.
    df = pd.read_csv('data/dataset.csv', sep=';')

    # SEGUNDO EJERCICIO.
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
