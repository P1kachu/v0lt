import socket

from v0ltlib.utils.v0lt_utils import fail, green, yellow, bytes_to_str


class Netcat:
    socket = None

    def __init__(self, hostname, port):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((hostname, port))
        except Exception as err:
            fail("Could not connect Netcat to {0}:{1} (error: {2})".format(hostname, port, err))
        print("Connected to port {0}".format(green(port)))

    def write(self, command):
        self.socket.send(bytes(command, "UTF-8"))

    def writeln(self, command):
        self.write(command + "\n")

    def shellcat(self, shellcode):
        shellcode = shellcode.replace("\\x", "")
        self.socket.send(bytearray.fromhex(shellcode))

    def shellcatln(self, shellcode):
        self.shellcat(shellcode + "\n")

    def read(self, nb_of_recv=1):
        data = "\n"
        for x in range(0, nb_of_recv):
            data += bytes_to_str(self.socket.recv(4096))
        return data

    def read_until(self, substring):
        data = "\n"
        while substring not in data:
            data += bytes_to_str(self.socket.recv(4096))
        return data

    def dialogue(self, command, nb_of_recv=1):
        self.writeln(command)
        return "{0}: {1}".format(yellow("Answer"), self.read(nb_of_recv))
