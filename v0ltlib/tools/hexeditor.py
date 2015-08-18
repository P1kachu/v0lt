import hexdump
from v0ltlib.utils.v0lt_utils import debug, bytes_to_str, str_to_bytes


class Hexeditor:
    chunks_size = 0
    chunks_separator = ''
    line_size = 0
    bytes_dump = ''
    string = ''
    bytes_per_line = 0

    def __init__(self, chunks_size=2, chunks_separator=' ', line_size=4):
        self.chunks_size = chunks_size
        self.chunks_separator = chunks_separator
        self.line_size = line_size
        self.bytes_per_line = self.line_size * self.chunks_size

    def dump_file(self, file_name):
        with open(file_name, "rb") as f:

            chunk = f.read(self.chunks_size)
            chunk_counter = 0
            actual_line = str_to_bytes("")

            while chunk:
                actual_line += chunk

                self.bytes_dump += hexdump.dump(chunk, self.chunks_size, self.chunks_separator)

                chunk_counter += 1
                chunk = f.read(self.chunks_size)

                if chunk_counter == self.bytes_per_line:
                    self.bytes_dump += "\n"
                    print(self.dump_string(actual_line))

                    actual_line = str_to_bytes("")
                    chunk_counter = 0

        return self.bytes_dump

    def dump_string(self, bytes_string):
        return hexdump.hexdump(bytes_string, "return")

    def save_file_as_hex(self, file_name):
        try:
            f = open(file_name, "w")
            f.write(self.bytes_dump)
        except FileNotFoundError as e:
            debug(e)

    def restore_file(self, file_name, source=None):
        if source:
            f = open(source, "r")
            to_restore = f.read()
            f.close()

        else:
            to_restore = self.bytes_dump

        try:
            f = open(file_name, "w")
            f.write(bytes_to_str(hexdump.restore(to_restore)))
            f.close()
        except FileNotFoundError as e:
            debug(e)
