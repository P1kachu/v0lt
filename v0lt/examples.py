import unittest

from v0lt import *

__author__ = 'P1kachu'


class Tests(unittest.TestCase):
    def test_netcat(self):
        nc = Netcat("archpichu.ddns.net", 65103)
        self.assertEqual(nc.read(), "\nNothing to display yet...\n")

    def test_telnet(self):
        tl = Telnet("archpichu.ddns.net", 65103)
        self.assertEqual(tl.read(), "\nNothing to display yet...\n")

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
        sh = ShellHack(70, "/bin/lol")
        sh.get_shellcodes(sh.keywords)
        sh = ShellHack(70, "/bin/sh")
        sh.get_shellcodes(sh.keywords)

    def test_flag_gen(self):
        flags_gen("flags.tmp", "P1ka", 10)

    def test_find_nth(self):
        self.assertEqual(find_nth("lolilol", "l", 3), 6)
        self.assertEqual(find_nth("lolilol", "l", 4), -1)

    def brute(self):
        bf = Bruteforce(charset="abcd", final_length=5, begin_with="l", end_with="P")
        bf.generate_strings()
        bf = Bruteforce(charset="abcdef", final_length=12, begin_with="l", end_with="P")
        bf.generate_strings(output="bf.tmp")

    def test_passwd_cracker(self):
        nix_basic_pass_cracker("HX9LLTdc/jiDE")
        nix_basic_pass_cracker("HX8LLTdc/jiDE")
        # nix_basic_pass_cracker("$1$khkWa1Nz$7YcmdOO1/uyHhMB7ga2L.1")
        # nix_basic_pass_cracker("$5$khkWa1Nz$583CsGZkoT82wh2ukf75KT4VVrf9ZO/P0FXLiPKgG//")
        # nix_basic_pass_cracker("$6$P1$XKg/SKZpe8Gbl5Utt3XVJEA4zJ6KB.IuZlShnP2FljfF32z3zoytnB.MaP9dJOObSOtiidHmeBp.feOqK4Mvg/")


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    unittest.TextTestRunner().run(suite)
