import unittest
from os import remove

from v0ltlib.utils.stack import Stack
from v0ltlib.utils.v0lt_utils import *
from v0ltlib.utils.crypto_utils import *

from v0ltlib.network.telnet import Telnet
from v0ltlib.network.netcat import Netcat

from v0ltlib.tools.shellhack import ShellHack
from v0ltlib.tools.bruteforce import Bruteforce

__author__ = 'P1kachu'


class Tests(unittest.TestCase):
    def test_netcat(self):
        nc = Netcat("archpichu.ddns.net", 65103)
        self.assertEqual(nc.read(1), "Nothing to display yet...\n")

    def test_telnet(self):
        tl = Telnet("archpichu.ddns.net", 65103)
        self.assertEqual(tl.read(1), "Nothing to display yet...\n")

    def test_stack(self):
        stack = Stack()
        self.assertEqual(stack.size(), 0)
        stack.push("item")
        self.assertEqual(stack.is_empty(), False)
        self.assertEqual(stack.size(), 1)
        item = stack.pop()
        self.assertEqual(stack.size(), 0)
        self.assertEqual(item, "item")
        self.assertEqual(stack.is_empty(), True)

    def test_basic_ceasar(self):
        plaintext = "This is a ceasar plaintext"
        encrypted = "GUVF VF N PRNFNE CYNVAGRKG"
        deciphered = basic_ceasar(plaintext, offset=13)
        self.assertEqual(encrypted, deciphered)

    def test_get_shellcode(self):
        sh = ShellHack(30, "x86", "bin/sh")
        sh.get_shellcodes(sh.keywords)

    def test_flag_gen(self):
        flags_gen("flags.tmp", "P1ka", 10)

    def test_find_nth(self):
        self.assertEqual(find_nth("lolilol", "l", 4), 6)

    def brute(self):
        bf = Bruteforce(charset="abcd", final_length=5, begin_with="l", end_with="P")
        bf.generate_strings()
        bf = Bruteforce(charset="abcdef", final_length=12, begin_with="l", end_with="P")
        bf.generate_strings(output="bf.tmp")


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    unittest.TextTestRunner().run(suite)
    input(prompt="Press any key to delete .tmp files")
    try:
        remove("*.tmp")
    except Exception as e:
        print(e)
