from faker import Faker
import re


def name_surname(df):
    '''Return the new dataframe with random names on column 'biker'.

    This function accepts a dataframe and returns an identical
    dataframe with the names on the column 'biker' changed by new
    random ones.

    Args:
        df (:obj:'DataFrame'): the DataFrame to be changed.

    Returns:
        df (:obj:'DataFrame'): the DataFrame with the biker names
        changed.
    '''
    # Cargamos la librería 'Faker' y creamos un bucle que cambia los
    # nombres de la columna por uno aleatorio.
    fake = Faker()
    for i in range(len(df)):
        df.loc[i, 'biker'] = fake.name()
    return df


def minutes_002040(t):
    '''Return a string with format 'hh:mm', where minutes can only be 00, 20 or 40.

    This function accepts a string in format 'hh:mm:ss' and returns another
    string in format 'hh:mm' where the minutes between 00 and 20 take value
    00, minutes between 20 and 40 take value 20 and the other minutes take
    value 40.

    Args:
        t (:obj:'string'): the string with format hh:mm:ss

    Returns:
        (:obj:'string'): the string with format hh:mm
    '''
    # Separamos la cadena por los ':'
    t = t.split(':')

    # Creamos un condicional que devuelve un valor diferente
    # en función del valor inicial de los segundos.
    if int(t[1]) < 20:
        return t[0] + ':00'
    elif int(t[1]) < 40:
        return t[0] + ':20'
    else:
        return t[0] + ':40'


def clean_club(club):
    '''Return a string without the substrings indicated.

    This function accepts a string a returns another one where
    the substrings in the variable 'replace_all', the substrings
    in the variable 'replace_beginnig' that are placed at the
    beginning of the string and the substrings in the variable
    'replace_end' that are placed at the end of the string are
    deleted.

    Args:
        club (:obj:'string'): the string to be cleaned

    Returns:
        club (:obj:'string'): the string cleaned
    '''
    # Definimos las subcadenas que queremos eliminar de la cadena.
    replace_all = ['PEÑA CICLISTA ', 'PENYA CICLISTA ',
                   'AGRUPACIÓN CICLISTA ', 'AGRUPACION CICLISTA ',
                   'AGRUPACIÓ CICLISTA ', 'AGRUPACIO CICLISTA ',
                   'CLUB CICLISTA ', 'CLUB ']
    replace_beginning = ['C.C. ', 'C.C ', 'CC ', 'C.D. ', 'C.D ',
                         'CD ', 'A.C. ', 'A.C ', 'AC ', 'A.D. ',
                         'A.D ', 'AD ', 'A.E. ', 'A.E ', 'AE ',
                         'E.C. ', 'E.C ', 'EC ', 'S.C. ', 'S.C ',
                         'SC ', 'S.D. ', 'S.D ', 'SD ']
    replace_end = [' T.T.', ' T.T', ' TT', ' T.E.', ' T.E', ' TE',
                   ' C.C.', ' C.C', ' CC', ' C.D.', ' C.D', ' CD',
                   ' A.D.', ' A.D', ' AD', ' A.C.', ' A.C', ' AC']

    # Ponemos en mayúsculas la cadena.
    club = club.upper()

    # Creamos un bucle que recorre la lista 'replace_all' y reemplazamos
    # por nada todas las veces que se repite cualquiera de las subcadenas
    # en la cadena inicial.
    for r_all in replace_all:
        club = re.sub(r_all, '', club)

    # Comprobamos si al principio de la cadena se encuentra la subcadena a
    # eliminar, y si es así, la reemplazamos por nada.
    # Utilizamos el caracter especial '\w\w\w' de las expresiones regulares
    # para indicar que a continuación de la subcadena debe haber al menos
    # 3 apariciones de caracteres que pueden formar parte de una palabra.
    for r_beg in replace_beginning:
        if re.search(r_beg + r'\w\w\w', club):
            club = re.sub(r_beg, '', club)

    # Realizamos lo mismo pero con las subcadenas a eliminar del final.
    # Aquí el caracter especial lo usamos para indicar que debe haber 3
    # caracteres antes de la subcadena.
    for r_end in replace_end:
        if re.search(r'\w\w\w' + r_end, club):
            club = re.sub(r_end, '', club)

    # Eliminamos espacios a principio y final.
    club = club.strip()

    return club