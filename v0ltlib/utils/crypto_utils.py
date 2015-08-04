import hashlib
import base64
import itertools

from v0ltlib.utils.v0lt_utils import red


def b64(s):
    return base64.b64decode(s)


def ceasar(string, offset=0):
    upper_bound = 128 - 32
    if offset != 0:
        encrypted = ''
        for each in string:
            p = 32 + ((ord(each) + offset) % upper_bound)
            encrypted += chr(p)
        return encrypted
    else:
        for i in range(0, upper_bound + 32):
            plaintext = ''
            for each in string:
                p = 32 + ((ord(each) - i) % upper_bound)
                plaintext += chr(p)
            print("{0}: {1}".format(i, plaintext))


def basic_ceasar(string, offset=0):
    string = string.upper()
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    upper_bound = len(alphabet)
    if offset != 0:
        encrypted = ''
        for c in string:
            if c == " ":
                encrypted += " "
            else:
                if c in alphabet:
                    encrypted += alphabet[(alphabet.index(c) + offset) % upper_bound]
        return encrypted
    else:
        for i in range(upper_bound, 0, -1):
            plaintext = ''
            for c in string:
                if c == " ":
                    plaintext += " "
                else:
                    if c in alphabet:
                        plaintext += alphabet[(alphabet.index(c) + i) % upper_bound]
            print("{0}: {1}".format(upper_bound - i, plaintext))


def sha1(s):
    return hashlib.sha1(s).hexdigest()


def sha256(s):
    return hashlib.sha256(s).hexdigest()


def md5(s):
    return hashlib.md5(s).hexdigest()


def xor_str(s, key):
    return "".join(chr(ord(c) ^ ord(k)) for c, k in zip(s, itertools.cycle(key)))


def str_inv_xor(key, xored):
    for i, char_xored in enumerate(xored):
        found = 0
        for char in range(32, 128):
            if char ^ ord(key[i]) == ord(char_xored):
                print(chr(char), end="")
                found = 1
                break
        if not found:
            print(red("X"), end="")


def int_inv_xor(key, xored):
    for i, char_xored in enumerate(xored):
        found = 0
        for char in range(32, 128):
            if char ^ key[i] == char_xored:
                print(chr(char), end="")
                found = 1
                break
        if not found:
            print(red("X"), end="")


def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient * x, x
        y, lasty = lasty - quotient * y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)


def gcd(a, b):
    a, b = (b, a) if a < b else (a, b)
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    return x % m


def totient(p, q):
    return (p - 1) * (q - 1)


def bitlength(x):
    assert x >= 0
    n = 0
    while x > 0:
        n += 1
        x >>= 1
    return n


def isqrt(n):
    if n < 0:
        raise ValueError('square root not defined for negative numbers')

    if n == 0:
        return 0
    a, b = divmod(bitlength(n), 2)
    x = 2 ** (a + b)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            return x
        x = y


def is_perfect_square(n):
    h = n & 0xF

    if h > 9:
        return -1

    # Take advantage of Boolean short-circuit evaluation
    if h != 2 and h != 3 and h != 5 and h != 6 and h != 7 and h != 8:
        t = isqrt(n)
        if t * t == n:
            return t
        else:
            return -1

    return -1


def inverse_power(x, n):
    high = 1
    while high ** n < x:
        high *= 2
    low = high / 2
    mid = 0
    while low < high:
        mid = int((low + high) // 2) + 1
        if low < mid and mid ** n < x:
            low = mid
        elif high > mid and mid ** n > x:
            high = mid
        else:
            return mid
    return mid + 1
