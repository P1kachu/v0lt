Tools
=====

##ShellCrafter
Craft shellcodes from ShellStorm, and send them easily via ShellCat!

```Python
>>> from v0lt import *
>>> shellhack = ShellCrafter(4096, "bin","execve")
>>> shellhack.get_shellcodes(shellhack.keywords)

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
>>> bf = Bruteforce(charset="abcd", final_length=4, begin_with="l", end_with="P")
>>> bf.generate_strings()
[ WARNING ] This may generate a very large output
(16 permutations here)
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

>>> bf = Bruteforce(charset="abcdef", final_length=10, begin_with="l", end_with="P")
>>> bf.generate_strings(output="bf.tmp")
[ WARNING ] This may generate a very large file
(1679616 permutations here == more than 17Mb)
[ DEBUG   ] Bruteforcing...
[ SUCCESS ] File created (19.2Mb)
```

##InstructionCounter
Defeat binaries using instruction counting

```python
>>> from v0lt import *
>>> counter = InstructionCounter('/home/pin', '/home/binary')
>>> counter.Accurate()
[!]WARNING  no length specified - guessing
[+]SUCCESS  Pass length guessed: 22
[+]SUCCESS  char guessed: I
[+]SUCCESS  char guessed: n
[+]SUCCESS  char guessed: S
[+]SUCCESS  char guessed: 7
[+]SUCCESS  char guessed: r
[+]SUCCESS  char guessed: u
[+]SUCCESS  char guessed: c
[+]SUCCESS  char guessed: t
[+]SUCCESS  char guessed: I
[+]SUCCESS  char guessed: 0
[+]SUCCESS  char guessed: n
[+]SUCCESS  char guessed: C
[+]SUCCESS  char guessed: o
[+]SUCCESS  char guessed: u
[+]SUCCESS  char guessed: n
[+]SUCCESS  char guessed: T
[+]SUCCESS  char guessed: i
[+]SUCCESS  char guessed: N
[+]SUCCESS  char guessed: 6
[+]SUCCESS  char guessed: R
[+]SUCCESS  char guessed: u
[+]SUCCESS  char guessed: l
[+]SUCCESS  char guessed: z
[+]SUCCESS  pass found: InS7ructI0nCounTiN6Rulz
```

