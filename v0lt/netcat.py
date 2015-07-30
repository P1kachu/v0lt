import socket
import subprocess

from v0lt.v0lt_utils import color, bytes_to_str


class Netcat:
    socket = None

    def __init__(self, hostname, port):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((hostname, port))
        except Exception as err:
            exit(color("Could not connect Netcat to {0}:{1} (error: {2})".format(hostname, port, err)))
        print("Connected to port {0}".format(color(port)))

    def write(self, command, shellcode=False):
        if shellcode:
            command = command.replace("\\x", "")
            self.socket.send(bytearray.fromhex(command))
        else:
            self.socket.send(bytes(command, "UTF-8"))

    def writeln(self, command, shellcode=False):
        command += "\n"
        if shellcode:
            command = command.replace("\\x", "")
            self.socket.send(bytearray.fromhex(command))
        else:
            self.socket.send(bytes(command, "UTF-8"))

    def read(self, nb_of_recv):
        data = "\n"
        for x in range(0, nb_of_recv):
            data += bytes_to_str(self.socket.recv(4096))
        return data

    def read_until(self, substring):
        data = "\n"
        while not substring in data:
            data += bytes_to_str(self.socket.recv(4096))
        return data

    def dialogue(self, command, nb_of_recv):
        self.writeln(command)
        return ("{0}: {1}").format(color("Answer"), self.read(nb_of_recv))