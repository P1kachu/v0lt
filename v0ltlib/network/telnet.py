import telnetlib

from v0ltlib.utils.v0lt_utils import fail, green, yellow, bytes_to_str


# WIP - SOME FEATURES NEED SOME REWORK


class Telnet:
    '''
    Quick Telnet implementation
    '''

    def __init__(self, hostname, port):
        '''
        Initialize a netcat client

        :param hostname: Hostname to connect to
        :param port:     Port to connect to
        '''

        try:
            self.tn = telnetlib.Telnet(hostname, port)
        except Exception as err:
            fail("Could not connect Telnet to {0}:{1} (error: {2})".format(hostname, port, err))
        print("Connected to port {0}".format(green(port)))

    def write(self, command):
        '''
        Send a message
        '''

        self.tn.write(bytes(command, "UTF-8"))

    def writeln(self, command):
        '''
        Send a message followed by a \n
        '''

        self.write(command + "\n")

    def shellnet(self, shellcode):
        '''
        Send a shellcode from the ShellCrafter
        '''

        shellcode = shellcode.replace("\\x", "")
        self.tn.write(bytearray.fromhex(shellcode))

    def read(self, nb_of_recv=1):
        '''
        Read from the server
        :param nb_of_recv: Number of message to try to receive
        :returns:    The received data
        '''

        data = "\n"
        for x in range(0, nb_of_recv):
            data += bytes_to_str(self.tn.read_some())
        return data

   def read_until(self, substring):
        '''
        Read until 'substring' is found

        :param substring: The string to look for
        :returns:         The received data
        '''

        return bytes.decode(self.tn.read_until(bytes(substring, "UTF-8")), "UTF-8")

    def dialogue(self, command, nb_of_recv=1):
        '''
        Exchange with the server
        Sends 'commands' and waits for 'nb_of_recv' messages back

        :param command:    message to send
        :param nb_of_recv: Number of messages to try to read
        :returns:          The received data
        '''

        self.writeln(command)
        return "{0}: {1}".format(yellow("Answer"), self.read(nb_of_recv))
