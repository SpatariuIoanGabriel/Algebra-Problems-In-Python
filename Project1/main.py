import itertools
# itertools is a module in Python's standard library which implies a collection of tools for working with iterable objects, like lists, tuples, and dictionaries


def associative_operations(n):
    if n <= 0 or n > 4:
        with open(out_file, "w") as _file:
            _file.write("The input for n is not correct!")
    else:
        # Generate a list of elements: [a1, a2, a3,..., an]
        elements = [f"a{i + 1}" for i in range(n)]

        # Determine all possible binary operation tables for n elements
        # itertools.product generates the cartesian product. range(n) returns numbers from 0 up to n-1. repeat=n ** 2 gives the length of each tuple. We use n ** 2 because we want square matrices
        possible_tables = list(itertools.product(range(n), repeat=n ** 2))

        # Check each table to see if it defines an associative operation
        associative_tables = []
        for table in possible_tables:
            is_associative = True
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        # Check associativity condition: a * (b * c) == (a * b) * c, where a, b, c belong to A
                        # Table is given as a one-dimensional array. Let x = a * (b * c) and y = (a * b) * c. In each table, we have the results after computing all the binary operations. In x, i and j act like rows and k acts like a column. In y, i acts like a row and j and k act like columns. For every element in A, we have an element in the operation table, given by a row and a column. table[j * n + k] and table[i * n + j] act like indices for the element we want to get from the operations table
                        x = table[i * n + table[j * n + k]]
                        y = table[table[i * n + j] * n + k]
                        if x != y:
                            is_associative = False
            if is_associative:
                associative_tables.append(table)

        # Count the number of associative operations and compute the operation tables
        number_of_operations = len(associative_tables)
        operation_tables = []
        for i in range(number_of_operations):
            # We take each associative_tables and compute the specific matrices, where j acts like a row and k acts like a column.
            matrix = [[associative_tables[i][j * n + k] for k in range(n)] for j in range(n)]
            operation_tables.append(matrix)

        # Print the output
        # The join() function concatenates all the elements together with a comma and a space between them
        with open(out_file, "w") as _file:
            _file.write(f"1. The number of associative operations on a set A = {{{', '.join(elements)}}} is {number_of_operations}\n")
            _file.write(f"2. The operation tables of the associative operations on A are:\n")
            for i in range(number_of_operations):
                # We use i + 1 to get the specific number of each operation table
                _file.write(f"\nTable {i + 1}:\n")
                for row in operation_tables[i]:
                    # Each operation table has n components
                    # elements[j] gives the element at j index
                    row_string = ', '.join(elements[j] for j in row)
                    _file.write(f"({row_string})\n")


in_file = "input_1.txt"
out_file = "output_1.txt"
with open(in_file, "r") as file:
    inp = file.readline()
associative_operations(int(inp))

in_file = "input_2.txt"
out_file = "output_2.txt"
with open(in_file, "r") as file:
    inp = file.readline()
associative_operations(int(inp))

in_file = "input_3.txt"
out_file = "output_3.txt"
with open(in_file, "r") as file:
    inp = file.readline()
associative_operations(int(inp))

in_file = "input_4.txt"
out_file = "output_4.txt"
with open(in_file, "r") as file:
    inp = file.readline()
associative_operations(int(inp))