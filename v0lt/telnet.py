import telnetlib

from v0lt_utils import color


class Telnet:
    tn = None

    def __init__(self, hostname, port):
        try:
            self.tn = telnetlib.Telnet(hostname, port)
        except Exception:
            exit("Could not connect telnet to {0}:{1}".format(hostname, port))
        print("{0}: {1}".format(color("Port " + str(port)), self.tn.read_all()))

    def write(self, command):
        self.tn.write(command)
        print(self.tn.read_all())

    def read(self, nb_of_recv, verbose=False):
        if verbose:
            for x in range(0, nb_of_recv):
                print(self.tn.read_until("\n"))
        else:
            for x in range(0, nb_of_recv):
                print(self.tn.read_until("\n"))
