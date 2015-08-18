import itertools
import random
import binascii
import struct

# Colors
RED = "\033[31;1m"
GREEN = "\033[32;1m"
YELLOW = "\033[33;1m"
BLUE = "\033[34;1m"
PURPLE = "\033[35;1m"
CYAN = "\033[36;1m"
WHITE = "\033[37;1m"
NONE = "\033[0m"

config = {"is_debug": True}


# String utils
def find_nth(string, substring, n):
    parts = string.split(substring, n + 1)
    if len(parts) <= n + 1:
        return -1
    return len(string) - len(parts[-1]) - len(substring)


def n_first(s, n):
    return s[:n]


def n_last(s, n):
    return s[n:]


# Output Formatting
def sizeof_fmt(num, suffix='b', rounded=False):
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%d%s%s" % (num, unit, suffix) if rounded else "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


def red(s):
    return str("{0}{1}{2}".format(RED, s, NONE))


def green(s):
    return str("{0}{1}{2}".format(GREEN, s, NONE))


def yellow(s):
    return str("{0}{1}{2}".format(YELLOW, s, NONE))


def blue(s):
    return str("{0}{1}{2}".format(BLUE, s, NONE))


def purple(s):
    return str("{0}{1}{2}".format(PURPLE, s, NONE))


def cyan(s):
    return str("{0}{1}{2}".format(CYAN, s, NONE))


def white(s):
    return str("{0}{1}{2}".format(WHITE, s, NONE))


def debug(s):
    if config.get("is_debug"):
        print("{0} {1}".format(purple("[ ]DEBUG   "), s))


def warning(s):
    print("{0} {1}".format(yellow("[!]WARNING "), s))


def fail(s):
    print("{0} {1}".format(red("[-]FAIL    "), s))


def success(s):
    print("{0} {1}".format(green("[+]SUCCESS "), s))


# Conversions
def bytes_to_hex(b):
    return hex_to_str(bytes_to_str(b))


def hex_to_bytes(s):
    return bytes_to_str(hex_to_str(s))


def str_to_bytes(s):
    return s.encode(encoding='UTF-8')


def bytes_to_str(b):
    return b.decode(encoding='UTF-8')


def str_to_hex(s):
    return binascii.hexlify(bytes(s, "UTfF-8"))


def hex_to_str(s):
    return bytes.fromhex(s).decode('utf-8')


def hex_to_little_endian(*args):
    return struct.pack("<{0}I".format(len(args)), *args)


def hex_to_big_endian(*args):
    return struct.pack(">{0}I".format(len(args)), *args)


# Random Utils
def flags_gen(output, head_of_flag, nb_of_flags):
    flag_size = 64
    alphabet = "ABCDEFabcdef0123456789"

    with open(output, 'w') as f:
        for i in range(nb_of_flags):
            flag = head_of_flag + "{"
            for j in range(flag_size):
                flag += alphabet[random.randint(0, len(alphabet) - 1)]
            flag += "}\n"
            f.write(flag)


def pow_two_align(size, alignment):
    if alignment != 0 and not alignment & (alignment - 1):
        return (size + alignment - 1) & ~(alignment - 1)
    else:
        fail("Not a power of two")


def is_query_success(response):
    return response.status_code // 10 == 20


def xor_bytes(b, key):
    if len(b) != len(key):
        warning("len(a) != len(b)")
    if len(b) > len(key):
        return str_to_hex("".join([chr(x ^ y) for (x, y) in zip(b[:len(key)], key)]))
    else:
        return str_to_hex("".join([chr(x ^ y) for (x, y) in zip(b, key[:len(b)])]))


def xor_str(s, key):
    return "".join(chr(ord(c) ^ ord(k)) for c, k in zip(s, itertools.cycle(key)))


def xor_hexa(h, key):
    return xor_bytes(hex_to_bytes(h), hex_to_bytes(key))
