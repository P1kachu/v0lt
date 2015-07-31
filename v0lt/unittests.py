import unittest
from os import remove

from v0lt.utils.crypto_utils import *
from v0lt.utils.v0lt_utils import *
from v0lt.Network.netcat import Netcat
from v0lt.Network.telnet import Telnet
from v0lt.utils.stack import Stack
import v0lt.Tools.Shellhack as Shellhack


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
        Shellhack.get_shellcodes("x86", "bin/sh")

    def test_flag_gen(self):
        flags_gen("test.tmp", "myCTF", 10)

    def test_find_nth(self):
        self.assertEqual(find_nth("lolilol", "l", 4), 6)


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    unittest.TextTestRunner().run(suite)
    remove("*.tmp")
