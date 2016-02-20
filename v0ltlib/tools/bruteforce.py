import itertools
import os

from v0ltlib.utils.v0lt_utils import fail, warning, debug, success, sizeof_fmt


class Bruteforce:
    dictionnary = ""
    range_limit = 0
    length = 0
    final_length = 0
    begin_with = ""
    end_with = ""
    max_iterations = 0

    def __init__(self, charset, final_length, begin_with="", end_with="", max_iterations=-1):
        self.dictionnary = charset
        self.range_limit = len(self.dictionnary)
        self.begin_with = begin_with
        self.end_with = end_with + "\n"
        self.final_length = final_length
        self.length = self.final_length - (len(self.begin_with) + len(self.end_with) - 1)
        self.max_iterations = max_iterations

    def generate_strings(self, output=None, verbose=True):
        nb_of_lines = pow(len(self.dictionnary), self.length)
        if self.max_iterations == -1:
            self.max_iterations = nb_of_lines + 1

        i = 0
        if output:
            f = open(output, "w")
            if verbose:
                approx_size = sizeof_fmt((self.final_length + 1) * nb_of_lines, rounded=True)
                warning("This may generate a very large file")
                print("({0} permutations here == more than {1})".format(nb_of_lines, approx_size))
                debug("Bruteforcing...")

            for n in range(self.length, self.length + 1):
                if i > self.max_iterations and self.max_iterations > 0:
                    break
                for perm in itertools.product(self.dictionnary, repeat=n):
                    i+=1
                    if i > self.max_iterations and self.max_iterations > 0:
                        break
                    bruted = ''.join(perm)
                    f.write(self.begin_with + bruted[::-1] + self.end_with)
            f.close()

            success("Bruted file created ({0})".format(sizeof_fmt(os.path.getsize(output))))

        else:
            if verbose:
                warning("This may generate a very large output")
                print("({0} permutations here)".format(nb_of_lines))

            for n in range(self.length, self.length + 1):
                for perm in itertools.product(self.dictionnary, repeat=n):
                    if i > self.max_iterations and self.max_iterations > 0:
                        break
                    i+=1
                    bruted = ''.join(perm)
                    print(self.begin_with + bruted[::-1] + self.end_with, end="")
                if i > self.max_iterations and self.max_iterations > 0:
                    break
