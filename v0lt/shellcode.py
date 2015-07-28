from requests import Request, Session
import json


def asm_to_shellcode(asm_file):
    with open(asm_file) as f:
        page = f.readlines()
        char_array = False
        shellcode = []
        for i, lines in enumerate(page):
            if "\"\\x" in lines:
                char_array = True
            if char_array:
                shellcode.append(lines[:lines.find("//")]) #delete comments
            else:
                page.remove(lines)
        print('[%s]' % '\n'.join(map(str, page)))

    return asm_file


def is_query_success(response):
    return response.status_code // 10 == 20


def dump_pretty_response(response):
    if is_query_success(response):
        try:
            print(json.dumps(response.json(), indent=4, ensure_ascii=False))
        except Exception:
            print("SUCCESS (code: {0})".format(response.status_code))
    else:
        print("ERROR (code: {0}) - {1}".format(response.status_code, response.text))


def get_shellcodes(*args):
    url = "http://shell-storm.org/api/?s="
    params = ""
    for arg in args:
        params += str(arg)
        params += "*"
    params = params[:len(params) - 1]
    s = Session()
    url += params
    req = Request("GET", url)
    prepped = req.prepare()
    resp = s.send(prepped, timeout=10, verify=True)
    dump_pretty_response(resp)
