import subprocess
import magic

from v0ltlib.utils.v0lt_utils import debug


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
