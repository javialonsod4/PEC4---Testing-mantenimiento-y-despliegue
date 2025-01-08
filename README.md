# PEC4_Alonso_Duran_Javier
Toma de contacto con archivos planos de Python (.py) y testeo y mantenimiento de funciones.

---
    Autor:
    - Javier Alonso Duran
---

Antes de poder ejecutar los archivos del proyecto, necesitarás tener instalado lo siguiente:

1. [Python](https://www.python.org/downloads/) (versión 3.6 o superior)
2. [pip](https://pip.pypa.io/en/stable/installation/) (generalmente viene con Python)

Y es aconsejable instalar también Pycharm, donde podrás ejecutar todos los archivos planos .py:
1. [PyCharm](https://www.jetbrains.com/help/pycharm/installation-guide.html#toolbox)

## Contenido

### Archivos

Este proyecto contiene diferentes archivos planos de Python (.py), una carpeta "data" que contiene el dataset que se estudia, una carpeta "img" que contiene un histograma creado en el propio proyecto, y el archivo de texto "requirements.txt" que contiene las versiones requeridas de librerías. Dentro de los archivos .py, encontramos primero un archivo llamado "utils.py" que contiene diferentes módulos creados para el proyecto. Luego un archivo "main.py" que contiene la resolución de todos los ejercicios en orden. Además, los archivos "ex1.py", "ex2.py", "ex3.py", "ex4.py" y "ex5.py", donde encontramos la resolución a cada ejercicio por separado. Finalmente, un último archivo "test.py" que testea o comprueba que los módulos realizan su función correctamente mediante una suite del módulo "unittest" de Python.

### Descripción del dataset

El dataset contiene la clasificación de la prueba de ciclismo de montaña (BTT) no competitiva *Orbea Monegros* realizada en Sariñena, Huesca, pero con los nombres de los ciclistas anonimizados.

## Ejecución

### Paso 1: Cargar los archivos en la carpeta del entorno virtual de PyCharm (carpeta .venv)

### Paso 2: Instalación de dependencias

Deberás abrir un terminal en PyCharm e ir a la carpeta del entorno vistual con el comando:

---
    cd .venv
---

Y desde aquí ejecutar lo siguiente:

---
    pip install -r requirements.txt
---

### Paso 3: Ejecución de archivos

En el propio terminal, y estando en la carpeta (.venv), ejecutaremos lo siguiente:

---
    python "archivo".py
---

Donde pone "archivo", deberás introducir el nombre el archivo. Por ejemplo, para ejecutar el archivo principal, que contiene la resolución al ejercicio completo, deberás ejecutar:

---
    python main.py
---

### Paso 4: Testeo de los módulos

Para comprobar que los módulos creados realizan su función, se debe ejecutar el archivo "test.py" de la siguiente manera:

---
    python test.py
---
Y el resultado deberá ser algo parecido a esto, si efectivamente realizan su función:

Loading dataset
test_clean_club (__main__.TestDataExpl.test_clean_club) ... Starting test_clean_club

ok

test_minutes_002040 (__main__.TestDataExpl.test_minutes_002040) ... Starting test_minutes_002040

ok

test_name_surname (__main__.TestDataExpl.test_name_surname) ... Starting test_name_surname

ok

----------------------------------------------------------------------
Ran 3 tests in 3.022s

OK

### Paso 5: Comprobación de seguimiento de estilo PEP8

Para comprobar que los diferentes archivos siguen la librería de estilo PEP8, debemos ejecutar en la terminal:

---
    pylint "archivo.py"
---
Esto nos devolverá los errores que hemos podido cometer en cuanto a limpieza del código en función de la librería.
