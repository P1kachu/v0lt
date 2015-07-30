import telnetlib

from v0lt.v0lt_utils import color, bytes_to_str


class Telnet:
    tn = None

    def __init__(self, hostname, port):
        try:
            self.tn = telnetlib.Telnet(hostname, port)
        except Exception as err:
            exit(color("Could not connect Telnet to {0}:{1} (error: {2})".format(hostname, port, err)))
        print("Connected to port {0}".format(color(port)))

    def write(self, command, shellcode=False):
        if shellcode:
            command = command.replace("\\x", "")
            self.tn.write(bytearray.fromhex(command))
        else:
            self.tn.write(bytes(command, "UTF-8"))

    def writeln(self, command):
        command += "\n"
        if shellcode:
            command = command.replace("\\x", "")
            self.tn.write(bytearray.fromhex(command))
        else:
            self.tn.write(bytes(command, "UTF-8"))

    def read(self, nb_of_recv):
        data = "\n"
        for x in range(0, nb_of_recv):
            data = bytes_to_str(self.tn.read_some())
        return data

    def read_until(self, substring):
        return bytes.decode(self.tn.read_until(bytes(substring, "UTF-8")), "UTF-8")

    def dialogue(self, command, nb_of_recv):
        self.writeln(command)
        return ("{0}: {1}").format(color("Answer"), self.read(nb_of_recv))
