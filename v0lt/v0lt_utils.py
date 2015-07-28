import itertools

RED = "\033[31;1m"
COLOR = "\033[34;1m"
NONE = "\033[0m"


def n_first(s, n):
    return s[:n]


def n_last(s, n):
    return s[n:]


def print_debug(s):
    print("{0}DEBUG".format(RED, s, NONE))


def color(s):
    return str("{0}{1}{2}".format(RED, s, NONE))


def bytes_to_hex(b):
    return hex_to_str(bytes_to_str(b))


def hex_to_bytes(s):
    return bytes_to_str(hex_to_str(s))


def str_to_bytes(s):
    return [ord(x) for x in s]


def bytes_to_str(b):
    return ''.join(chr(x) for x in b)


def str_to_hex(s):
    return s.encode('hex')


def hex_to_str(s):
    return s.decode('hex')


def xor_bytes(b, key):
    if len(b) != len(key):
        print("len(a) != len(b)")
    if len(b) > len(key):
        return "".join([chr(x ^ y) for (x, y) in zip(b[:len(key)], key)]).encode('hex')
    else:
        return "".join([chr(x ^ y) for (x, y) in zip(b, key[:len(b)])]).encode('hex')


def xor_str(s, key):
    return "".join(chr(ord(c) ^ ord(k)) for c, k in zip(s, itertools.cycle(key)))


def xor_hexa(h, key):
    return xor_bytes(hex_to_bytes(h), hex_to_bytes(key))
