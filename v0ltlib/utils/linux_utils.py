import subprocess
import crypt
import magic
import passlib.hash as passlib
from v0ltlib.utils.v0lt_utils import debug, warning, success, fail, cyan


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

    # Basic MD5
    if crypt_method == '0':
        salt = encrypted_pass[0:2]

        debug("Password: {0}".format(encrypted_pass))
        debug("Salt: {0}".format(salt))

        dict_file = open("common_passwords.txt", "r")
        for word in dict_file.readlines():
            word = word.rstrip()
            if encrypted_pass == crypt.crypt(word, salt=salt):
                success("Password corresponding to {0} is {1}."
                        .format(encrypted_pass, cyan(word)))
                return word

    # /etc/shadow style
    else:
        if crypt_method == '1':
            debug("Method: MD5")
            encryption = passlib.md5_crypt.encrypt
            pass_filter = lambda x: x
        elif crypt_method == '5':
            debug("Method: SHA256")
            encryption = passlib.sha256_crypt.encrypt
            pass_filter = filter_rounds
            warning("This may be long... Go grab a coffee (or maybe 10)")
        elif crypt_method == '6':
            debug("Method: SHA512")
            encryption = passlib.sha512_crypt.encrypt
            pass_filter = filter_rounds
            warning("This may be long... Go grab a coffee (or maybe 10)")
        else:
            fail("Unknown encryption method.")
            return

        salt = encrypted_pass.split("$")[2]

        debug("Password: {0}".format(encrypted_pass))
        debug("Salt: {0}".format(salt))

        dict_file = open("common_passwords.txt", "r")
        for word in dict_file.readlines():
            word = word.rstrip()
            if encrypted_pass == pass_filter(encryption(word, salt=salt)):
                success("Password corresponding to {0} is {1}."
                        .format(encrypted_pass, cyan(word)))
                return word

    fail("Password not found for {0}.".format(encrypted_pass))
    return


def filter_rounds(password):
    pass_list = password.split("$")
    filtered = "${0}${1}${2}".format(pass_list[1], pass_list[3], pass_list[4])
    return filtered
