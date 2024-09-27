import time
import matplotlib.pyplot as plt

# Gramática en Forma Normal de Chomsky (CNF)
cnf_grammar = {
    'S': [('A', 'B'), ('B', 'C')],
    'A': [('B', 'A'), 'a'],
    'B': [('C', 'C'), 'b'],
    'C': [('A', 'B'), 'a']
}

# Función para el algoritmo CYK
def cyk_algorithm(grammar, string):
    n = len(string)
    if n == 0:  # Verificar si la cadena está vacía
        return False

    table = [[set() for _ in range(n)] for _ in range(n)]

    # Inicialización
    for i, char in enumerate(string):
        for lhs, productions in grammar.items():
            for production in productions:
                if len(production) == 1 and production[0] == char:
                    table[i][i].add(lhs)

    # Rellenar la tabla
    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            for split in range(start, end):
                for lhs, productions in grammar.items():
                    for production in productions:
                        if len(production) == 2:
                            left, right = production
                            if left in table[start][split] and right in table[split + 1][end]:
                                table[start][end].add(lhs)

    # Verificar si la cadena pertenece al lenguaje
    return 'S' in table[0][n - 1]

# Leer las cadenas desde el archivo
def read_strings_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Medir el tiempo de ejecución y graficar
def measure_and_plot_times(strings, grammar):
    lengths = []
    times = []

    for index, string in enumerate(strings, 1):  # Añadimos un índice para la numeración de las cadenas
        if len(string) == 0:  # Saltar cadenas vacías
            continue
        
        start_time = time.time()
        accepted = cyk_algorithm(grammar, string)
        elapsed_time = time.time() - start_time

        # Mostrar en consola la cadena, si fue aceptada o no, y el tiempo de ejecución
        print(f"{index}. Cadena: '{string}'")
        print(f"   - Aceptada: {'Sí' if accepted else 'No'}")
        print(f"   - Tiempo de ejecución: {elapsed_time:.6f} segundos\n")

        lengths.append(len(string))
        times.append(elapsed_time)

    # Graficar los resultados
    plt.plot(lengths, times, marker='o')
    plt.title('Tiempo de ejecución del algoritmo CYK')
    plt.xlabel('Número de caracteres en la cadena')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.grid(True)
    plt.show()

# Ejecución directa
file_path = 'cadenas.txt'
strings = read_strings_from_file(file_path)
measure_and_plot_times(strings, cnf_grammar)




