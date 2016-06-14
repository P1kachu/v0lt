from v0lt import *

ic = InstructionCounter('./pin/', 'examples/inscount_example.elf')

password = ic.Accurate()

assert password == 'InS7ructI0nCounTiN6Rulz'
