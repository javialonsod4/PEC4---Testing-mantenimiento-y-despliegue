'''This module test the functions defined in the archive "utils.py"'''

import unittest
import pandas as pd
from utils import name_surname, minutes_002040, clean_club


class TestDataExpl(unittest.TestCase):
    '''This class contains the different tests to the functions in
    "utils.py".'''

    @classmethod
    def setUpClass(cls):
        '''This function loads the dataset.'''
        print("Loading dataset")
        cls._df = pd.read_csv("data/dataset.csv", sep=";")

    def test_name_surname(self):
        '''This function tests the function "name_surname".'''
        print('Starting test_name_surname')
        # Importamos el dataframe en una nueva variable para que no se
        # modifique al aplicar la función.
        df_0 = pd.read_csv('data/dataset.csv', sep=';')
        df_1 = name_surname(self._df)
        self.assertNotEqual(df_0.loc[0, 'biker'], df_1.loc[0, 'biker'])

    def test_minutes_002040(self):
        '''This function tests the function "minutes_002040".'''
        print('Starting test_minutes_002040')
        # Comprobamos que devuelve el valor que debería para los 3
        # posibles casos.
        self.assertEqual(minutes_002040('01:19:23'), '01:00')
        self.assertEqual(minutes_002040('03:21:1'), '03:20')
        self.assertEqual(minutes_002040('06:40:00'), '06:40')

    def test_clean_club(self):
        '''This function tests the function "clean_club".'''
        print('Starting test_clean_club')
        self.assertEqual(clean_club('C.c. Alfinden'), 'ALFINDEN')
        self.assertEqual(clean_club('SIGÜES C.C.'), 'SIGÜES')
        self.assertEqual(clean_club('Club Ciclista Saidi'), 'SAIDI')


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDataExpl)
    unittest.TextTestRunner(verbosity=2).run(suite)
