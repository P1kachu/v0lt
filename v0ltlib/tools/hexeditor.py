import hexdump
from v0ltlib.utils.v0lt_utils import debug, bytes_to_str


class Hexeditor:
    chunks_size = 0
    chunks_separator = ''
    dump = ''
    string = ''

    def __init__(self, chunks_size=2, chunks_separator=''):
        self.chunks_size = chunks_size
        self.chunks_separator = chunks_separator

    def dump_file(self, file_name):
        self.dump = hexdump.dump(file_name, self.chunks_size, self.chunks_separator)

    def dump_string(self, string):
        self.string = hexdump.hexdump(bytes(string, "UTF-8"))

    def save_file(self, file_name):
        try:
            f = open(file_name, "w")
            f.write(hexdump.restore(bytes_to_str(self.dump)))
        except FileNotFoundError as e:
            debug(e)
