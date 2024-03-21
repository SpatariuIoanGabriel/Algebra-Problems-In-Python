import itertools
# itertools is a module in Python's standard library which implies a collection of tools for working with iterable objects, like lists, tuples, and dictionaries


def abelian_subgroups(m, n):
    with open(out_file, "w") as _file:
        if (m or n) < 2 or (m or n) > 10:
            _file.write("The input is not correct!")
        else:
            # We compute the Cartesian product of Zm and Zn.
            ZmZn = [(i, j) for i in range(m) for j in range(n)]

            # We compute the powerset of ZmZn.
            powerset = []
            for t in range(1, len(ZmZn) + 1):
                # t represents the length of each tuple in powerset. Using itertools.combinations, we compute all possible combinations of elements from ZmZn.
                powerset.extend(itertools.combinations(ZmZn, t))

            # We check each subset of ZmZn for closure under addition.
            subgroups = []
            for subset in powerset:
                closed = True
                for ii in range(len(subset)):
                    for j in range(ii, len(subset)):
                        # ii and j are indices of pairs from each subset. k represents any element from any pair. The zip() function aggregates elements from two or more iterables and returns an iterator of tuple. k takes values from 0 up to len(subset[ii]) - 1. The tuple (m, n) gives the values of p. We use % p to ensure the fact that after performing the addition, first element is not greater than m and the second one is not greater than n. We use tuple() to ensure that the final result is a tuple.
                        sum_ = tuple((subset[ii][k] + subset[j][k]) % p for k, p in zip(range(len(subset[ii])), (m, n)))
                        if sum_ not in subset:
                            # We use break to exit the inner loop when the condition is met.
                            closed = False
                            break
                    if not closed:
                        break
                if closed:
                    subgroups.append(subset)

            # Here we form the output.
            output = []
            for x, subgroup in enumerate(subgroups):
                # We check if one subgroup is equal to ZmZn to write the subgroup as a cartesian product. set() function converts the result into a set.
                if set(subgroup) == set(ZmZn):
                    output.append(f"H{x + 1} = " + "Z" + str(m) + "x" + "Z" + str(n))
                else:
                    # The join() function concatenates all the tuples together.
                     output.append(f"H{x + 1} = " + "{" + ", ".join([str(tuple_) for tuple_ in subgroup]) + "}")

            _file.write(f"1. The number of subgroups of the abelian group (Z{m}xZ{n}, +) is {len(subgroups)}.\n\n"
                    f"2. The subgroups of the abelian group (Z{m}xZ{n}, +) are:\n\n" + "\n".join(output))

in_file = "input_1.txt"
out_file = "output_1.txt"
with open(in_file, "r") as file:
    inp_1 = file.readline()
    inp_2 = file.readline()
abelian_subgroups(int(inp_1), int(inp_2))

in_file = "input_2.txt"
out_file = "output_2.txt"
with open(in_file, "r") as file:
    inp_1 = file.readline()
    inp_2 = file.readline()
abelian_subgroups(int(inp_1), int(inp_2))

in_file = "input_3.txt"
out_file = "output_3.txt"
with open(in_file, "r") as file:
    inp_1 = file.readline()
    inp_2 = file.readline()
abelian_subgroups(int(inp_1), int(inp_2))

in_file = "input_4.txt"
out_file = "output_4.txt"
with open(in_file, "r") as file:
    inp_1 = file.readline()
    inp_2 = file.readline()
abelian_subgroups(int(inp_1), int(inp_2))

in_file = "input_5.txt"
out_file = "output_5.txt"
with open(in_file, "r") as file:
    inp_1 = file.readline()
    inp_2 = file.readline()
abelian_subgroups(int(inp_1), int(inp_2))


