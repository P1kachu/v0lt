import subprocess
import magic
import crypt

from v0ltlib.utils.v0lt_utils import debug, success, fail


def nix_echo(to_echo, params):
    bash_command = "echo -{0} {1}".format(params, to_echo)
    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    return output


def nix_file(file):
    try:
        with magic.Magic() as m:
            return m.id_filename(file)
    except Exception as e:
        debug(e)


# From Violent Python
def nix_basic_pass_cracker(encrypted_pass):
    crypt_method = encrypted_pass.split("$")[1]
    print(crypt_method)
    if crypt_method == '1':
        crypt.METHOD_CRYPT = crypt.METHOD_MD5
    elif crypt_method == '5':
        crypt.METHOD_CRYPT = crypt.METHOD_SHA256
    elif crypt_method == '6':
        crypt.METHOD_CRYPT = crypt.METHOD_SHA512
    else:
        fail("Unknown encryption method")
        return

    salt = encrypted_pass.split("$")[2]
    print(salt)

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
