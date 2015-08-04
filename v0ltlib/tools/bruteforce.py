from v0ltlib.utils.v0lt_utils import red
import itertools


class Bruteforce:
    dictionnary = ""
    range_limit = 0
    length = 0
    begin_with = ""
    end_with = ""

    def __init__(self, charset, final_length, begin_with="", end_with=""):
        self.dictionnary = charset
        self.range_limit = len(self.dictionnary)
        self.begin_with = begin_with
        self.end_with = end_with + "\n"
        self.length = final_length - (len(self.begin_with) + len(self.end_with) - 1)
        if len(charset) > final_length:
            exit(red("Charset length should be less than length"))

    def generate_brute_strings(self, output=None):
        f = None
        nb_of_lines = pow(len(self.dictionnary), self.length)
        print(red("BE CAREFULL - This may generate a very large file ({0} lines here)".format(nb_of_lines)))
        if output:
            f = open(output, "w")
            for n in range(self.length, self.length + 1):
                for perm in itertools.product(self.dictionnary, repeat=n):
                    f.write(self.begin_with + ''.join(perm) + self.end_with)
        else:
            for n in range(self.length, self.length + 1):
                for perm in itertools.product(self.dictionnary, repeat=n):
                    print(self.begin_with + ''.join(perm) + self.end_with, end="")


if __name__ == "__main__":
    bf = Bruteforce("abcd", 4, "l", "P")
    bf.generate_brute_strings()
