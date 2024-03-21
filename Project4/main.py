import numpy as np
# numpy is a Python library used for working with arrays. numpy provides us a wide range of mathematical functions
from itertools import product
# itertools is a module in Python's standard library which implies a collection of tools for working with iterable objects, like lists, tuples, and dictionaries


def order(matrix):
    # Here we calculate the determinant of the matrix using .linalg.det to determine if the matrix is invertible.
    det = np.linalg.det(matrix)
    if det == 0:
        return None
    else:
        order = 1
        m = matrix
        while not np.all(m == np.eye(len(matrix), dtype=np.uint8)):
            # We check if matrix m is equal to the identity matrix.
            # np.eye(len(matrix), dtype=np.uint8) creates the identity matrix of the same size as the input matrix. The dtype=np.uint8 argument specifies that the data type of the matrix elements should be unsigned 8-bit integers. Using an 8-bit unsigned  integer data type is sufficient and help us save memory.
            # np.all compares each element of m with the corresponding element in the identity matrix
            m = np.dot(m, matrix) % 2
            # Perform matrix multiplication between m and the input matrix.
            # np.dot performs matrix multiplication
            # We perform % 2 operation to keep the resulting matrix containing only elements of 0 or 1.
            order += 1
            # Increment the order by 1 in each iteration
            # The order keeps track of the number of iterations performed, representing the order of the matrix
    return order

def gl_n_z_2(n):
    matrices = []
    # Create an empty list to store the matrices

    # Generate all possible combinations of 0 and 1 with a length of n**2. We use n**2 because we want square matrices.
    # The product function from itertools generates the Cartesian product of the given iterable
    # Here, it generates all possible combinations of 0 and 1 repeated n**2 times
    for x in product([0, 1], repeat=n**2):
        # Convert the combination of x into a numpy array.
        # We use .reshape to reshape the array into a square matrix of size n x n.
        matrix = np.array(x, dtype=np.uint8).reshape(n, n)
        # We check if the determinant of the matrix % 2 is not equal to 0
        # If the determinant % 2 is not 0, we add the matrix to the list.
        if np.linalg.det(matrix) % 2 != 0:
            matrices.append(matrix)
    return matrices


def gl_n_z_2_order(n):
    if n < 2 or n > 5:
        with open(out_file, "w") as _file:
            _file.write("The input for n is not correct!")
    else:
        group = gl_n_z_2(n)
        with open(out_file, "w") as _file:
            _file.write(f"1. The order of the group (GL{n}(Z2),·) is {len(group)} and its elements are:\n")
            for matrix in group:
                # We write the string representation of the matrix to the file
                _file.write(np.array2string(matrix, separator=' ', prefix=''))
                _file.write("\n\n")
                # We add new lines after each matrix.

            _file.write(f"2. The orders of the elements of the group (GL{n}(Z2),·):\n")
            for matrix in group:
                # We calculate the order of the matrix.
                o = order(matrix)
                # Convert the matrix to a string representation with indentation.
                # We use separator=' ' to control the spacing between matrix elements and prefix='    ' to align the rows one under the other.
                matrix_str = np.array2string(matrix, separator=' ', prefix='    ')
                _file.write("ord({}) = {}".format(matrix_str, o))
                _file.write("\n\n")


in_file = "input_1.txt"
out_file = "output_1.txt"
with open(in_file, "r") as file:
    inp = file.readline()
gl_n_z_2_order(int(inp))

in_file = "input_2.txt"
out_file = "output_2.txt"
with open(in_file, "r") as file:
    inp = file.readline()
gl_n_z_2_order(int(inp))

in_file = "input_3.txt"
out_file = "output_3.txt"
with open(in_file, "r") as file:
    inp = file.readline()
gl_n_z_2_order(int(inp))

in_file = "input_4.txt"
out_file = "output_4.txt"
with open(in_file, "r") as file:
    inp = file.readline()
gl_n_z_2_order(int(inp))
