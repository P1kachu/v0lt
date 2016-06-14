import itertools
import os
from v0ltlib.utils.v0lt_utils import *
from v0ltlib.tools.bruteforce import Bruteforce

class InputForm:
    STDIN = 1
    ARGV = 2

class StopAt:
    HIGHEST_COUNT = 1
    FIRST_CHANGE = 2

class InstructionCounter:
    """
    Password cracker using instruction counting tool based on Intel Pin
    """

    PIN64_COMMAND = '{0}pin -t {0}source/tools/ManualExamples/obj-intel64/inscount0.so -- '
    PIN32_COMMAND = '{0}pin -t {0}source/tools/ManualExamples/obj-ia32/inscount0.so -- '
    OUTPUT_FILE = 'inscount.out'
    TMP_BRUTE = 'tmp_bruteforce'
    PIN_STRING_BEGIN = 'Count '
    USUAL_CHARSET = "._abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}[]-=+*^%$@!."

    def __init__(self,
                 pin_path,
                 binary_name,
                 verbose=False,
                 arch=64,
                 input_form=InputForm.ARGV,
                 stop_at=StopAt.FIRST_CHANGE,
                 length=-1,
                 charset=USUAL_CHARSET):

        self.binary = binary_name
        self.arch = arch
        self.input_form = input_form
        self.stop_at = stop_at
        self.length = length
        self.charset = charset

        config['is_debug'] = verbose

        if arch == 32:
            self.cmd = self.PIN32_COMMAND.format(pin_path)
        else:
            self.cmd = self.PIN64_COMMAND.format(pin_path)

    def clean_temp(self):
        if os.path.isfile(self.TMP_BRUTE):
            os.remove(self.TMP_BRUTE)
        if os.path.isfile(self.OUTPUT_FILE):
            os.remove(self.OUTPUT_FILE)
        if os.path.isfile('pin.log'):
            os.remove('pin.log')

    def run_pin(self, string):
        if self.input_form == InputForm.ARGV:
            cmd = '{0} {1} {2}'.format(self.cmd, self.binary, string)
            os.system(cmd)
        else:
            cmd = '/bin/bash -c "{0} {1} <<< {2}"'.format(self.cmd, self.binary, string)
            os.system(cmd)

    def get_pass_length(self):

        iterations = -1
        max_i = 0

        for i in range(2, 100):

            string = 'A' * i
            self.run_pin(string)

            try:
                with open(self.OUTPUT_FILE, 'r') as f:
                    count = f.read()
                    count = count[len(self.PIN_STRING_BEGIN):]
                    count = int(count)
                    debug("Count: {0}".format(count))
                    if iterations < 0:
                        iterations = count
                    else:
                        if iterations < count:
                            iterations = count
                            if self.stop_at == StopAt.FIRST_CHANGE:
                                success('Pass length guessed: {0}'.format(i))
                                return i
                            max_i = i
            except Exception as e:
                smth_went_wrong('get_pass_length', e)
                return -1

        success('Pass length guessed: {0}'.format(max_i))
        self.clean_temp()
        return max_i

