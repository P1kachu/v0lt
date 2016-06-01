import itertools
import os

from v0ltlib.utils.v0lt_utils import fail, warning, debug, success, sizeof_fmt


class Bruteforce:
    '''
    Easy bruteforce generator
    '''

    def __init__(self, charset, final_length, begin_with="", end_with="", max_iterations=-1):
        self.dictionnary = charset
        self.range_limit = len(self.dictionnary)
        self.begin_with = begin_with
        self.end_with = end_with + "\n"
        self.final_length = final_length
        self.length = self.final_length - (len(self.begin_with) + len(self.end_with) - 1)
        self.max_iterations = max_iterations

    def generate(self):
        '''
        Generator that will yield each permutation, one at a time

        :returns: Strings
        '''
        i = 0
        for n in range(self.length, self.length + 1):

            if i > self.max_iterations and self.max_iterations > 0:
                break

            for perm in itertools.product(self.dictionnary, repeat=n):
                i+=1
                if i > self.max_iterations and self.max_iterations > 0:
                    break
                bruted = ''.join(perm)
                bruted = self.begin_with + bruted[::-1] + self.end_with
                yield bruted

    def generate_strings(self, output=None, verbose=True):
        '''
        Generate strings for printing to screen or to a file

        :param output:  If set, name of the file to write the permutations to
        :param verbose: Display or not the classical warning messages
        '''
        nb_of_lines = pow(len(self.dictionnary), self.length)
        if self.max_iterations == -1:
            self.max_iterations = nb_of_lines + 1

        if output:

            f = open(output, "w")

            if verbose:
                approx_size = sizeof_fmt((self.final_length + 1) * nb_of_lines, rounded=True)
                warning("This may generate a very large file")
                print("({0} permutations here == more than {1})".format(nb_of_lines, approx_size))
                debug("Bruteforcing...")
            for bruted in self.generate():
                f.write(bruted)

            f.close()
            success("Bruted file created ({0})".format(sizeof_fmt(os.path.getsize(output))))

        else:
            if verbose:
                warning("This may generate a very large output")
                print("({0} permutations here)".format(nb_of_lines))

            for bruted in self.generate():
                print(bruted)
