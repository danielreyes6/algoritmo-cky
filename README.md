# Algoritmo CYK con Gramática en Forma Normal de Chomsky (CNF)

Este proyecto implementa el algoritmo CYK (Cocke-Younger-Kasami) para verificar si una cadena pertenece a un lenguaje definido por una gramática en Forma Normal de Chomsky (CNF). Además, mide y grafica el tiempo de ejecución para diferentes cadenas.

## Requisitos

Asegúrate de tener instaladas las siguientes dependencias antes de ejecutar el código:

- Python 3.x
- matplotlib (para la graficación)

Para instalar `matplotlib`, puedes usar el siguiente comando:

    bash
    pip install matplotlib


Descripción del código

    Gramática en CNF: La gramática está definida en el diccionario cnf_grammar con las reglas de producción correspondientes en forma binaria o terminal.

    Función cyk_algorithm(): Implementa el algoritmo CYK que toma una gramática en CNF y una cadena de entrada. Construye una tabla triangular para verificar si la cadena es aceptada por la gramática.

    Función read_strings_from_file(): Lee cadenas desde un archivo de texto, eliminando espacios innecesarios al principio o al final de cada línea.

    Función measure_and_plot_times(): Ejecuta el algoritmo CYK para cada cadena leída, midiendo el tiempo de ejecución y graficando la relación entre la longitud de la cadena y el tiempo de procesamiento.

Uso

Archivo de entrada: Crea un archivo de texto llamado cadenas.txt con las cadenas que deseas verificar. Cada cadena debe estar en una línea separada.
Ejemplo del archivo cadenas.txt:

    ab
    aba
    bbaa

Ejecutar el código: Simplemente ejecuta el script en Python.

    bash
  
    python3 algoritmo.py

Salida: El código imprimirá los resultados de la evaluación de cada cadena en la consola, indicando si fue aceptada por la gramática y el tiempo de ejecución. Además, generará una gráfica que muestra el tiempo de ejecución en función del número de caracteres de cada cadena.

Ejemplo de salida:

markdown

    1. Cadena: 'ab'
       - Aceptada: Sí
       - Tiempo de ejecución: 0.000032 segundos

    2. Cadena: 'aba'
       - Aceptada: No
       - Tiempo de ejecución: 0.000054 segundos

Personalización

    Gramática: Puedes modificar la gramática en CNF directamente en el diccionario cnf_grammar para adaptarla a otras reglas gramaticales.
    Cadenas de prueba: Modifica el archivo cadenas.txt para agregar las cadenas que deseas probar.

Gráfica de resultados

La gráfica resultante muestra el tiempo de ejecución del algoritmo CYK en función de la longitud de cada cadena de entrada. Esto te permite visualizar la eficiencia del algoritmo a medida que la longitud de las cadenas aumenta.
