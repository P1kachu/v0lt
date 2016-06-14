import socket

from v0ltlib.utils.v0lt_utils import fail, green, yellow, bytes_to_str


class Netcat:
    """
    Easy and quick interface for emulating netcat, with possibility to send
    shellcodes directly from ShellCrafter !
    """
    def __init__(self, hostname, port):
        """
        Initialize a netcat client

        :param hostname: Hostname to connect to
        :param port:     Port to connect to
        """

        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((hostname, port))
        except Exception as err:
            fail("Could not connect Netcat to {0}:{1} (error: {2})".format(hostname, port, err))
            raise err
        print("Connected to port {0}".format(green(port)))

    def write(self, command):
        """
        Send a message
        """

        self.socket.send(bytes(command, "UTF-8"))

    def writeln(self, command):
        """
        Send a message followed by a \n
        """

        self.write(command + "\n")

    def shellcat(self, shellcode):
        """
        Send a shellcode from the ShellCrafter
        """

        shellcode = shellcode.replace("\\x", "")
        self.socket.send(bytearray.fromhex(shellcode))

    def read(self, nb_of_recv=1):
        """
        Read from the server
        :param nb_of_recv: Number of message to try to receive
        :returns:    The received data
        """

        data = "\n"
        for x in range(0, nb_of_recv):
            data += bytes_to_str(self.socket.recv(4096))
        return data

    def read_until(self, substring):
        """
        Read until 'substring' is found

        :param substring: The string to look for
        :returns:         The received data
        """

        data = "\n"
        while substring not in data:
            data += bytes_to_str(self.socket.recv(4096))
        return data

    def dialogue(self, command, nb_of_recv=1):
        """
        Exchange with the server
        Sends 'commands' and waits for 'nb_of_recv' messages back

        :param command:    message to send
        :param nb_of_recv: Number of messages to try to read
        :returns:          The received data
        """

        self.writeln(command)
        return "{0}: {1}".format(yellow("Answer"), self.read(nb_of_recv))
