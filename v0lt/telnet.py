import telnetlib

from v0lt_utils import color


class Telnet:
    tn = None

    def __init__(self, hostname, port):
        try:
            self.tn = telnetlib.Telnet(hostname, port)
        except Exception as err:
            exit(color("Could not connect Telnet to {0}:{1} (error: {2})".format(hostname, port, err)))
        print("Port {0}: {1}".format(color(port), self.tn.read_all()))

    def write(self, command):
        self.tn.write(bytes(command, "UTF-8"))
        print(self.tn.read_all())

    def read(self, nb_of_recv, verbose=False):
        if verbose:
            for x in range(0, nb_of_recv):
                print(self.tn.read_until("\n"))
        else:
            for x in range(0, nb_of_recv):
                self.tn.read_until("\n")
