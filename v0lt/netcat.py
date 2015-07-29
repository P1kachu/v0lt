import socket

from v0lt_utils import color


class Netcat:
    socket = None

    def __init__(self, hostname, port):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((hostname, port))
        except Exception as err:
            exit(color("Could not connect Netcat to {0}:{1} (error: {2})".format(hostname, port, err)))
        print("Port {0}: {1}".format(color(port), self.socket.read(4096)))

    def write(self, command):
        self.socket.send(bytes(command, "UTF-8"))
        print(self.socket.recv(4096))

    def read(self, nb_of_recv, verbose=False):
        if verbose:
            for x in range(0, nb_of_recv):
                print(self.socket.recv(4096))
        else:
            for x in range(0, nb_of_recv):
                self.socket.recv(4096)
