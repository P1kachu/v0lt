import itertools
import os
import crypt

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

        if len(charset) > final_length:
            fail("Charset length should be smaller than strings length.")

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


# From Violent Python
def nix_basic_pass_cracker(encrypted_pass, crypt_method=crypt.METHOD_SHA512):
    crypt.METHOD_CRYPT = crypt_method
    salt = encrypted_pass[:2]

    # Common passwords first
    dict_file = open("../utils/common_passwords.txt", "r")
    for word in dict_file.readlines():
        to_test = crypt.crypt(word, salt)

        if to_test == encrypted_pass:
            success("Password corresponding to {0} is {1}.".format(encrypted_pass, to_test))
            return to_test

    dict_file = open("/usr/share/dict/words", "r")
    for word in dict_file.readlines():
        to_test = crypt.crypt(word, salt)

        if to_test == encrypted_pass:
            success("Password corresponding to {0} is {1}.".format(encrypted_pass, to_test))
            return to_test

    fail("Password not found.")
    return
