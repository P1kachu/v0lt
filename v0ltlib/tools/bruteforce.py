import itertools
import os

from v0ltlib.utils.v0lt_utils import red, green, sizeof_fmt


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

        if len(charset) > final_length:
            exit(red("Charset length should be smaller than strings length"))

    def generate_brute_strings(self, output=None):
        nb_of_lines = pow(len(self.dictionnary), self.length)
        approx_size = sizeof_fmt((self.final_length + 1) * nb_of_lines, rounded=True)

        if output:
            approx_size = sizeof_fmt((self.final_length + 1) * nb_of_lines, rounded=True)

            print(red("BE CAREFULL - This may generate a very large file "), end="")
            print("({0} permutations here ~ {1})".format(nb_of_lines, approx_size))
            f = open(output, "w")
            for n in range(self.length, self.length + 1):
                for perm in itertools.product(self.dictionnary, repeat=n):
                    f.write(self.begin_with + ''.join(perm) + self.end_with)
            f.close()
            print(green("File created ({0})".format(sizeof_fmt(os.path.getsize(output)))))

        else:
            print(red("BE CAREFULL - This may generate a very large output "), end="")
            print("({0} permutations here)".format(nb_of_lines))
            for n in range(self.length, self.length + 1):
                for perm in itertools.product(self.dictionnary, repeat=n):
                    print(self.begin_with + ''.join(perm) + self.end_with, end="")


if __name__ == "__main__":
    bf = Bruteforce(charset="abcd", final_length=4, begin_with="l", end_with="P")
    bf.generate_brute_strings()
    bf = Bruteforce(charset="abcdef", final_length=10, begin_with="l", end_with="P")
    bf.generate_brute_strings(output="bf.tmp")
