import subprocess
import crypt
import magic
import passlib.hash as passlib
from v0ltlib.utils.v0lt_utils import debug, success, fail, cyan


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


def nix_basic_pass_cracker(encrypted_pass):
    try:
        crypt_method = encrypted_pass.split("$")[1]
    except Exception:
        crypt_method = '0'
    # I don't like switches anyway
    if crypt_method == '0':
        salt = encrypted_pass[0:2]

        debug("Password: {0}".format(encrypted_pass))
        debug("Salt: {0}".format(salt))

        dict_file = open("common_passwords.txt", "r")
        for word in dict_file.readlines():
            to_test = crypt.crypt(word.rstrip(), salt=salt)

            if to_test == encrypted_pass:
                success("Password corresponding to {0} is {1}."
                        .format(encrypted_pass, cyan(word.rstrip())))
                return to_test

        dict_file = open("/usr/share/dict/words", "r")
        for word in dict_file.readlines():
            to_test = crypt.crypt(word.rstrip(), salt=salt)
            if to_test == encrypted_pass:
                success("Password corresponding to {0} is {1}."
                        .format(encrypted_pass, cyan(word.rstrip())))
                return to_test

        fail("Password not found for {0}.".format(encrypted_pass))
        return

    else:
        if crypt_method == '1':
            encryption = passlib.md5_crypt.encrypt
            pass_filter = lambda x: x
        elif crypt_method == '5':
            encryption = passlib.sha256_crypt.encrypt
            pass_filter = filter_rounds
        elif crypt_method == '6':
            encryption = passlib.sha512_crypt.encrypt
            pass_filter = filter_rounds
        else:
            fail("Unknown encryption method.")
            return

        salt = encrypted_pass.split("$")[2]

        debug("Password: {0}".format(encrypted_pass))
        debug("Salt: {0}".format(salt))

        dict_file = open("common_passwords.txt", "r")
        for word in dict_file.readlines():
            to_test = encryption(word.rstrip(), salt=salt)
            to_test = pass_filter(to_test)
            if to_test == encrypted_pass:
                success("Password corresponding to {0} is {1}."
                        .format(encrypted_pass, cyan(word.rstrip())))
                return to_test

        dict_file = open("/usr/share/dict/words", "r")
        for word in dict_file.readlines():
            to_test = encryption(word.rstrip(), salt=salt)
            to_test = pass_filter(to_test)

            if to_test == encrypted_pass:
                success("Password corresponding to {0} is {1}."
                        .format(encrypted_pass, cyan(word.rstrip())))
                return to_test

        fail("Password not found for {0}.".format(encrypted_pass))
        return


def filter_rounds(password):
    pass_list = password.split("$")
    ret = "${0}${1}${2}".format(pass_list[1], pass_list[3], pass_list[4])
    return ret
