import telnetlib

from v0lt_utils import color, bytes_to_str


class Telnet:
    tn = None

    def __init__(self, hostname, port):
        try:
            self.tn = telnetlib.Telnet(hostname, port)
        except Exception as err:
            exit(color("Could not connect Telnet to {0}:{1} (error: {2})".format(hostname, port, err)))
        print("Connected on port {0}".format(color(port)))

    def write(self, command):
        self.tn.write(bytes(command, "UTF-8"))
        data = bytes_to_str(self.tn.read_all())
        print(data)
        return data

    def read(self, nb_of_recv, verbose=False):
        if verbose:
            for x in range(0, nb_of_recv):
                data = bytes_to_str(self.tn.read_some())
                print(data)
                return data
        else:
            for x in range(0, nb_of_recv):
                return bytes_to_str(self.tn.read_some())
