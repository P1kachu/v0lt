Tools
=====

##ShellHack   
Used to send easily shellcodes via netcat

```Python
>>> from v0lt import *
>>> shellhack = ShellHack(4096, "bin","execve")

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
Your choice: http://shell-storm.org/shellcode/files/shellcode-752.php
Shellcode: "\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62[...]"

>>> nc.shellcat(shellhack.shellcode)
>>> padded_shellcode = shellhack.pad()
```

##Bruteforce  
Easy bruteforce generator

```Python
>>> from v0lt import *
>>> bf = Bruteforce(4096, "bin","execve")
>>> f = Bruteforce(charset="abcde", final_length=4, begin_with="l", end_with="P")
>>> bf.generate_brute_strings()
BE CAREFULL - This may generate a very large file (16 lines here)
laaP
labP
lacP
ladP
lbaP
lbbP
lbcP
lbdP
lcaP
lcbP
lccP
lcdP
ldaP
ldbP
ldcP
lddP
>>> bf.generate_brute_strings(output="bf.tmp")
```
