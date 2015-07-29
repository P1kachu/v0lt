import socket

from v0lt.v0lt_utils import color, bytes_to_str


class Netcat:
    socket = None

    def __init__(self, hostname, port):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((hostname, port))
            self.socket.settimeout(25)
        except Exception as err:
            exit(color("Could not connect Netcat to {0}:{1} (error: {2})".format(hostname, port, err)))
        print("Connected on port {0}".format(color(port)))

    def write(self, command):
        self.socket.send(bytes(command, "UTF-8"))

    def writeln(self, command):
        self.socket.send(bytes(command + "\n", "UTF-8"))
        data = bytes_to_str(self.socket.recv(4096))
        print(data)
        return data

    def read(self, nb_of_recv):
        data = ""
        for x in range(0, nb_of_recv):
            data += bytes_to_str(self.socket.recv(4096))
        return data

    def read_until(self, substring):
        data = ""
        while not substring in data:
            data += bytes_to_str(self.socket.recv(4096))
        return data