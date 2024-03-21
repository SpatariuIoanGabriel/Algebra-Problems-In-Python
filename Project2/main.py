import itertools
# itertools is a module in Python's standard library which implies a collection of tools for working with iterable objects, like lists, tuples, and dictionaries


def is_abelian(m):
    # m is a matrix
    n = len(m)
    # n is the number of rows/columns in the matrix m
    for row in m:
        # we check if m is a square matrix
        if len(row) != n:
            return False
    for i in range(n):
        for j in range(n):
            # Here we check the commutative condition. Basically, we take an element in the operation table at row i and column j, and we compare it with other element in the operation table at row j and column i. If the elements are equal, the commutative condition is satisfied.
            if m[i][j] != m[j][i]:
                return False
    return True


def is_associative(m):
    # m is a matrix
    n = len(m)
    # n is the number of rows/columns in the matrix m
    for row in m:
        # we check if m is a square matrix
        if len(row) != n:
            return False
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if m[m[i][j]-1][k] != m[i][m[j][k]-1]:
                    # Here we check the associativity condition. On the left side, i acts like rows and j and k act like columns. On the right side, i and j act like rows and k acts like columns. We subtract 1 because we want indexing to start from 0.
                    return False
    return True


def has_identity_element(m):
    # m is a matrix
    n = len(m)
    # n is the number of rows/columns in the matrix m
    for i in range(n):
        if all(m[i][j] == j for j in range(n)) and all(m[j][i] == j for j in range(n)):
            # Here we check the identity element condition. We take an element in operation table at row i and column j and another element in operation table at row j and column i. If the elements are equal between them and equal to j, for any i and j in range(n), the identity element
            # condition is satisfied.
            return True
    return False


def abelian_group_structures(n):
    # Generate a list of elements: [a1, a2, a3,..., an]
    elements = [f"a{i + 1}" for i in range(n)]
    print(elements)
    with open(out_file, "w") as _file:
        if n <= 0:
            _file.write("The input for n is not correct!")
        count = 0
        operation_tables = []
        # Determine all possible binary operation tables for n elements
        # itertools.product generates the cartesian product. range(n) returns numbers from 0 up to n-1. repeat=n ** 2 gives the length of each tuple. We use n ** 2 because we want square matrices
        _file.write(f"1.The abelian group structures on G are given by the matrices:\n")
        possible_tables = list(itertools.product(range(n), repeat=n ** 2))
        print(possible_tables)
        for i in range(len(possible_tables)):
            # We take each member of possible_tables and compute the specific matrices, where j acts like a row and k acts like a column.
            matrix = [[possible_tables[i][j * n + k] for k in range(n)] for j in range(n)]
            print(matrix)
            if is_abelian(matrix) and has_identity_element(matrix) and is_associative(matrix):
                operation_tables.append(matrix)
                count += 1
                _file.write(f"\nStructure {count}:\n")
                for ii in range(n):
                    # We add a parenthesis before each row.
                    _file.write("(")
                    for jj in range(n):
                        # ii and jj are from 0 up to n-1, where ii acts like a row and jj acts like a column.
                        # matrix[ii][jj] gives the element at row ii and column jj.
                        # We use + 1 to get the specific number of each element.
                        _file.write("a" + str(matrix[ii][jj] + 1))
                        if jj < n - 1:
                            # We add space between elements.
                            _file.write(" ")
                    # We close the parenthesis after each for loop.
                    _file.write(")\n")

        # The join() function concatenates all the elements together with a comma and a space between them
        _file.write(f"\n2.The number of abelian group structures on a set G = {{{', '.join(elements)}}} is {count}.\n")


in_file = "input_1.txt"
out_file = "output_1.txt"
with open(in_file, "r") as file:
    inp = file.readline()
abelian_group_structures(int(inp))

in_file = "input_2.txt"
out_file = "output_2.txt"
with open(in_file, "r") as file:
    inp = file.readline()
abelian_group_structures(int(inp))

in_file = "input_3.txt"
out_file = "output_3.txt"
with open(in_file, "r") as file:
    inp = file.readline()
abelian_group_structures(int(inp))

in_file = "input_4.txt"
out_file = "output_4.txt"
with open(in_file, "r") as file:
    inp = file.readline()
abelian_group_structures(int(inp))

in_file = "input_5.txt"
out_file = "output_5.txt"
with open(in_file, "r") as file:
    inp = file.readline()
abelian_group_structures(int(inp))

abelian_group_structures(2)