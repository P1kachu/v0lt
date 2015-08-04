import subprocess

import magic


def echo(to_echo, params):
    bash_command = "echo -{0} {1}".format(params, to_echo)
    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    return output


def file(file):
    with magic.Magic() as m:
        m.id_filename(file)
