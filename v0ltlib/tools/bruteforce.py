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

    def __init__(self, charset, final_length, begin_with="", end_with=""):
        self.dictionnary = charset
        self.range_limit = len(self.dictionnary)
        self.begin_with = begin_with
        self.end_with = end_with + "\n"
        self.final_length = final_length
        self.length = self.final_length - (len(self.begin_with) + len(self.end_with) - 1)

    def generate_strings(self, output=None):
        nb_of_lines = pow(len(self.dictionnary), self.length)

        if output:
            approx_size = sizeof_fmt((self.final_length + 1) * nb_of_lines, rounded=True)

            warning("This may generate a very large file")
            print("({0} permutations here == more than {1})".format(nb_of_lines, approx_size))

            f = open(output, "w")
            debug("Bruteforcing...")
            for n in range(self.length, self.length + 1):
                for perm in itertools.product(self.dictionnary, repeat=n):
                    f.write(self.begin_with + ''.join(perm) + self.end_with)
            f.close()

            success("File created ({0})".format(sizeof_fmt(os.path.getsize(output))))

        else:
            warning("This may generate a very large output")
            print("({0} permutations here)".format(nb_of_lines))
            for n in range(self.length, self.length + 1):
                for perm in itertools.product(self.dictionnary, repeat=n):
                    print(self.begin_with + ''.join(perm) + self.end_with, end="")
