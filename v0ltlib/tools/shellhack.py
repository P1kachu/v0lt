from urllib.request import urlopen

from requests import Session, Request

from bs4 import BeautifulSoup
from v0ltlib.utils.v0lt_utils import fail, yellow, cyan, find_nth, is_query_success


class ShellHack:
    length = 0
    maximum_shellcode_length = 0
    keywords = None
    shellcode = ""

    def __init__(self, maximum_length, *keywords, shellcode=None):
        self.maximum_shellcode_length = maximum_length
        self.keywords = keywords
        self.shellcode = shellcode
        if not shellcode and not keywords:
            exit(fail("Please specify some shellcode or keywords"))

    @staticmethod
    def delete_comments(line):
        if "//" in line:
            comment = line.find("//")
            line = line[:comment]
        if "/*" in line:
            comment = line.find("/*")
            line = line[:comment]
        if "*/" in line:
            comment = line.find("*/")
            line = line[:comment]
        return line

    def html_to_shellcode(self, link):
        # Fetch webpage
        html = urlopen(link).read()

        # Extract text
        soup = BeautifulSoup(html, "html.parser")
        for script in soup(["script", "style"]):
            script.extract()
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)

        # Extract shellcode
        shellcode = []
        for i, line in enumerate(text.split("\n")):
            if "\"\\x" in line:
                line = self.delete_comments(line)
                line = line[line.find("\"\\x"):]
                shellcode.append(line)

        # Clean Shellcode
        final_shellcode = ''.join(shellcode)
        final_shellcode = final_shellcode.replace("\"", "")
        final_shellcode = final_shellcode.replace(";", "")
        final_shellcode = final_shellcode.replace(" ", "")
        final_shellcode = final_shellcode.replace("\t", "")
        final_shellcode = final_shellcode.replace("\n", "")
        print("{0} {1}\n".format(yellow("Shellcode:"), final_shellcode))

        # Return shellcode as string, not bytes
        self.shellcode = final_shellcode.replace("\\x", "\\\\x")
        return self.shellcode

    @staticmethod
    def handle_shelllist(response_text):
        response_text_list = [x for x in response_text.split("\n") if x]
        shellist = []
        print("\n")

        if len(response_text_list) < 1:
            fail("No shellcode found for these parameters.")
            return None

        for i, line in enumerate(response_text_list):
            # Get shellcode architecture
            architecture = line[line.find("::::") + 4:find_nth(line, "::::", 1)]

            # Get shellcode's name
            title = line[find_nth(line, "::::", 1) + 4:find_nth(line, "::::", 2)]

            # Get shellcode's link
            link = line[find_nth(line, "::::", 3) + 4:]

            # Add to list
            entry = "({0}) {1}".format(architecture, cyan(title))
            shellist.append(link)
            print("{0}: {1}".format(i, entry))

        user_choice = 0
        while 1:
            user_choice = input(yellow("Selection: "))
            if int(user_choice) < 0:
                continue
            try:
                print("Your choice: {0}".format(shellist[int(user_choice)]))
                break
            except IndexError:
                continue

        # Return selected shellcode
        return shellist[int(user_choice)]

    def get_shellcodes(self, args):
        url = "http://shell-storm.org/api/?s="

        # Craft URL with parameters
        params = ""
        for arg in args:
            params += str(arg)
            params += "*"
        params = params[:len(params) - 1]
        url += params

        # Request
        req = Request("GET", url)
        prepped = req.prepare()
        s = Session()
        resp = s.send(prepped, timeout=10, verify=True)
        link = ""
        if is_query_success(resp):
            link = self.handle_shelllist(resp.text)
        else:
            exit("Something went wrong with the request ({0}: {1}".format(resp.code, resp.text))

        # Get Shellcode
        return self.html_to_shellcode(link) if link else link

    def shellcode_length(self):
        return int(len(self.shellcode) / 4)

    def pad(self):
        pad_length = self.maximum_shellcode_length - self.shellcode_length()
        return "A" * pad_length
