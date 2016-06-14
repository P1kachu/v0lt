import os
import unittest

from v0lt import *

__author__ = 'P1kachu'


class Tests(unittest.TestCase):
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
        sh = ShellCrafter(70, "/bin/lol")
        sh.get_shellcodes(sh.keywords)
        sh = ShellCrafter(70, "/bin/sh", script_index=98)
        sh.get_shellcodes(sh.keywords)

    def test_flag_gen(self):
        outpt = "flags.tmp"
        flags_gen(outpt, "P1ka", 10)
        os.remove(outpt)

    def test_find_nth(self):
        self.assertEqual(find_nth("lolilol", "l", 3), 6)
        self.assertEqual(find_nth("lolilol", "l", 4), -1)

    @staticmethod
    def brute():
        outpt = "bf.tmp"
        bf = Bruteforce(charset="abcd", final_length=5, begin_with="l", end_with="P")
        bf.generate_strings()
        bf = Bruteforce(charset="abcdef", final_length=12, begin_with="l", end_with="P")
        bf.generate_strings(output=outpt)
        os.remove(outpt)


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    unittest.TextTestRunner().run(suite)
