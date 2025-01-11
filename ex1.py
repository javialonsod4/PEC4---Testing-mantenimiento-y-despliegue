'''This module solves exercise 1.'''

import pandas as pd

if __name__ == "__main__":

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
