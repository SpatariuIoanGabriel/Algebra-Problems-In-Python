from itertools import permutations
# itertools is a module in Python's standard library which implies a collection of tools for working with iterable objects, like lists, tuples, and dictionaries

def calculate_permutation_group(n):
    if n < 2 or n > 6:
        with open(out_file, "w") as _file:
            _file.write("The input for n is not correct!")
    else:
        # We compute the set of permutations using itertools.permutations. We take the range from 1 up to n + 1, because we want to work with all numbers from 1 up to n.
        perms = tuple(permutations(range(1, n + 1)))

        # We compute the identity permutation as a tuple of numbers from 1 up to n.
        e = tuple(range(1, n + 1))

        with open(out_file, "w") as _file:
            _file.write(f"1. The elements of the group (S{n}, ◦) are:\n\n")
            for i, p in enumerate(perms):
                if i == 0:
                    # We write the identity permutation.
                    _file.write(f"e = {e}\n")
                    _file.write(f"    {e}\n")
                    _file.write("\n")
                else:
                    cycles = []
                    # We compute a set to keep track of visited elements.
                    visited = set()

                    # Find the cycles in the permutation
                    for j in range(1, n + 1):
                        if j not in visited:
                            cycle = []
                            # We set the starting point of a cycle to the current element j.
                            k = j
                            while k not in cycle:
                                # We add the current element to the cycle.
                                cycle.append(k)
                                # We mark the element as visited.
                                visited.add(k)
                                # We subtract 1 from k to adjust the index to 0.
                                k = p[k - 1]
                            if len(cycle) > 1:
                                # The join() function concatenates all the elements together.
                                cycles.append(" ".join(str(x) for x in cycle))

                    # We convert the cycles to a string representation.
                    cycle_str = " ".join(["({})".format(cycle) for cycle in cycles])

                    # The format() method is used to format strings by replacing {} with corresponding values.
                    _file.write("σ{} = {}\n".format(i, e))
                    _file.write("     {} = {}\n".format(tuple(p), cycle_str))
                    _file.write("\n")

            _file.write(f"2. The orders of the elements of the group (S{n}, ◦) are:\n\n")

            # Calculate and write the order of each permutation
            for i, p in enumerate(perms):
                # We initialize the order with 1.
                order = 1
                # Here we assign the current permutation to x.
                x = p
                while x != e:
                    # Apply the permutation to each element in x. Basically, we apply the permutation p by accessing the appropriate elements based on the values in x. We save the values with tuple().
                    x = tuple(p[j-1] for j in x)
                    # Here we increment the order by 1.
                    order += 1
                if i == 0:
                    _file.write("ord(e) = {}\n".format(order))
                else:
                    _file.write("ord(σ{}) = {}\n".format(i, order))

in_file = "input_1.txt"
out_file = "output_1.txt"
with open(in_file, "r") as file:
    inp = file.readline()
calculate_permutation_group(int(inp))

in_file = "input_2.txt"
out_file = "output_2.txt"
with open(in_file, "r") as file:
    inp = file.readline()
calculate_permutation_group(int(inp))

in_file = "input_3.txt"
out_file = "output_3.txt"
with open(in_file, "r") as file:
    inp = file.readline()
calculate_permutation_group(int(inp))

in_file = "input_4.txt"
out_file = "output_4.txt"
with open(in_file, "r") as file:
    inp = file.readline()
calculate_permutation_group(int(inp))

in_file = "input_5.txt"
out_file = "output_5.txt"
with open(in_file, "r") as file:
    inp = file.readline()
calculate_permutation_group(int(inp))
